from django.shortcuts import render
from django.views.generic import (FormView, CreateView, RedirectView, View, DetailView, ListView, UpdateView, TemplateView)
# Create your views here.

class LandingPage(TemplateView):
    template_name = 'index.html'

class Registration(TemplateView):
    template_name = 'register.html'

class Login(TemplateView):
    template_name = 'login.html'