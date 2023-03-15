from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CreationForm


# Create your views here.

class SignUp(CreateView):
    form_class = CreationForm

    success_url = reverse_lazy('meal_app:index')
    template_name = 'users/signup.html'


def user_acount(request):
    template = 'users/lk.html'
    return render(request, template)
