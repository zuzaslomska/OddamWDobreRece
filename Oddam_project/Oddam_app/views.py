from django.shortcuts import render
from django.views.generic import (FormView, CreateView, RedirectView, View, DetailView, ListView, UpdateView, TemplateView)
from Oddam_app.forms import RegistrationForm


class LandingPage(TemplateView):
    template_name = 'index.html'

class Registration(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()

        return super(Registration,self).form_valid(form)

class Login(TemplateView):
    template_name = 'login.html'