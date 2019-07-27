from django.conf.urls import url
from . import views
app_name = 'game'
urlpatterns = [
    url(r'^home/', views.match_list, name='match_list'),
    url(r'^detail/(?P<match_id>\d+)/$', views.match_detail, name='match_detail'),
    url(r'^detail/(?P<match_id>\d+)/pay/$', views.pay, name='pay'),
    url(r'^result/$', views.result, name='result'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^contact_us/$',views.contact_us,name='contact_us'),
    url(r'^refer/$',views.refer,name='refer'),
    url(r'^earn/$',views.earn,name='earn'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^$',views.home,name='home'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
]