from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='users/auth.html',
                          next_page='meal_app:index'),
        name='login'
    ),
    path(
        "logout/", LogoutView.as_view(template_name="users/logout.html",
                          next_page='meal_app:index'),
        name="logout"
    ),
    path('password_change/',
         PasswordChangeView.as_view(template_name='users/change_password.html'),
         name='password_change'),

]
