from django import forms
from game.models import UserProfileInfo
from django.contrib.auth.models import User
from django.forms import RadioSelect

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('gender', 'phone')
        widgets = {
            'gender' : RadioSelect()
        }
class EditUserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)