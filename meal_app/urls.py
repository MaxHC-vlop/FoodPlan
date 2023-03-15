from django.urls import path
from . import views

app_name = 'meal_app'

urlpatterns = [
    path('', views.index, name='index'),
    # path('auth/', views.auth, name='auth'),
    path('registration/', views.registration, name='registration'),
    path('order/', views.order, name='order'),
]
