from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (FormView, CreateView, RedirectView, View, DetailView, ListView, UpdateView, TemplateView)
from Oddam_app.forms import RegistrationForm, LoginForm
from Oddam_app.models import MyUser


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


class GiveawayView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'form.html'

class Administration(ListView):
    template_name = 'administration.html'
    queryset = MyUser.objects.filter(is_superuser=True)

class AdminUpdate(UpdateView):
    model = MyUser
    fields = ['first_name','last_name','email','is_superuser']
    template_name = 'myuser_update_form.html'