from django.shortcuts import render

def index(request):
    template = 'meal_app/index.html'
    return render(request, template)

def auth(request):
    template = 'meal_app/auth.html'
    return render(request, template)