from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name='User'
urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('signup/',views.sign_up,name='signup'),
    path('logout/',views.log_out,name='logout'),
    path('password_change/',auth_views.PasswordChangeView.as_view(success_url='/User/login/'),
         {'template_name': 'User/templates/registration/password_change_form.html'},name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),
         {'template_name': 'User/templates/registration/password_change_done.html'},name='password_change_done'),
    ]