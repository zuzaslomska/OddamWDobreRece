from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Oddam_app.models import MyUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['password1','password2','email','first_name','last_name']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Imię',
                                                                'name': 'name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Nazwisko',
                                                                'name': 'surname'})
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder': 'Email',
                                                             'name': 'email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Hasło',
                                                                     'name': 'password1'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Powtórz Hasło',
                                                                     'name': 'password2'})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Email',
                                                             'name':'email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Hasło',
                                                                     'name': 'password'})
