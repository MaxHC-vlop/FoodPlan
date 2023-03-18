from django.urls import path
from . import views

app_name = 'meal_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<recipe_id>/', views.recipe, name='recipe'),
    path('order/', views.order, name='order'),
]
