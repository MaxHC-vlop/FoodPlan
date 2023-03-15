from django.shortcuts import render

def index(request):
    template = 'meal_app/index.html'
    return render(request, template)

def order(request):
    template = 'meal_app/order.html'
    return render(request, template)