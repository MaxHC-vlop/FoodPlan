from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='users/auth.html'),
        name='login'
    ),

    path('password_change/',
         PasswordChangeView.as_view(template_name='users/change_password.html'),
         name='password_change'),

]
