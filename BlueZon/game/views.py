from django.shortcuts import render, get_object_or_404, redirect
from game.models import Match, UserProfileInfo, FreePayUser
from django.contrib.auth.models import User
from game.forms import UserForm,UserProfileInfoForm,EditUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
#for email verification
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
import time

def home(request):
    if(request.user.username):
        print(request.user)
        return redirect('../home')
    return render(request, 'game/home.html')
def match_list(request):
    matchs = Match.objects.filter(available = True)
    context = {
        'matchs' : matchs,
        'nbar' : 'home'
    }
    return render(request, 'game/matchs/list.html', context)
def match_detail(request, match_id):
    detail = get_object_or_404(Match, id=match_id)
    freepay = FreePayUser.objects.filter(matchid=match_id)
    usr = detail.users
    users = usr.split(',')
    join = 'no'
    uname = request.user.username
    for u in users:
        if u == uname:
            join = 'yes'
    for free in freepay:
        if free.users == uname:
            join = 'yes'
    if detail.entry == 100:
        join = 'full'
    context = {
        'detail' : detail,
        'users' : users,
        'join' : join,
        'remove_nav' : 'remove_nav',
        'nbar' : 'home'
    }
    return render(request, 'game/matchs/detail.html', context)
def result(request):
    context = {
        'nbar' : 'result'
    }
    return render(request, 'game/matchs/result.html', context)
def pay(request, match_id):
    detail = get_object_or_404(Match, id=match_id)
    uname = request.user.username
    FreePayUser.objects.create(matchid=match_id, users = uname)
    usr = detail.users
    users = usr.split(',')
    context = {
        'detail' : detail,
        'users' : users,
        'join' : 'yes',
        'remove_nav' : 'remove_nav',
        'nbar' : 'home'
    }
    return render(request, 'game/matchs/detail.html', context)
def profile(request):
    i = request.user.id
    user = get_object_or_404(User, id=i)
    prof = get_object_or_404(UserProfileInfo, user_id=i)
    context = {
        'user' : user,
        'profile' : prof,
        'nbar' : 'profile'
    }
    return render(request, 'game/matchs/profile.html', context)
def edit_profile(request):
    i = request.user.id
    if request.method == 'POST':
        user = EditUserForm(request.POST, instance=request.user)
        prof = UserProfileInfoForm(request.POST, instance=request.user)
        if user.is_valid() and prof.is_valid():
            user.save()
            prof.save()
            return redirect('../profile')
    else:
        user = get_object_or_404(User, id=i)
        prof = get_object_or_404(UserProfileInfo, user_id=i)
    context = {
        'user' : user,
        'profile' : prof,
        'nbar' : 'profile'
    }
    return render(request, 'game/profile/edit_profile.html', context)
def contact_us(request):
    context = {
        'nbar' : 'profile'
    }
    return render(request, 'game/profile/contact_us.html', context)
def refer(request):
    context = {
        'nbar' : 'profile'
    }
    return render(request, 'game/profile/refer.html', context)
def earn(request):
    context = {
        'nbar' : 'earn'
    }
    return render(request, 'game/matchs/earn.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('../../../')
def register(request):
    error = 'noerror'
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            user.save()
            #email verifiation
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            #set extra data to UserProfileInfo
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponse('<br><br><center><h1>Please confirm your email address to complete the registration.</h1><br><h2 style="color: red">Please Check your SPAM folder for verification Mail.</h2></center>')
        else:
            error = "error"
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'game/login/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'error':error})
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('<br><br><center><h1>Thank you for your email confirmation. Now you can login your account.</h1><h2>Click <a href="https://www.bluezon.ml/home/">Here</a> to LogIn.</h2></center>')
    else:
        return HttpResponse('Activation link is invalid!')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('../home')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'game/login/login.html', {'error':'error'})
    else:
        return render(request, 'game/login/login.html', {'error':'noerror'})