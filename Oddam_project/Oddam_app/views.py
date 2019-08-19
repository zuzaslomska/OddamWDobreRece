from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import (FormView, CreateView, RedirectView, View, DetailView, ListView, UpdateView, TemplateView)
from Oddam_app.forms import RegistrationForm, LoginForm


class LandingPage(TemplateView):
    template_name = 'index.html'

class Registration(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()

        return super(Registration,self).form_valid(form)


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('giveaway')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class GiveawayView(TemplateView):
    template_name = 'form.html'