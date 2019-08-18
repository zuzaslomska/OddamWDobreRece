from django import forms
from django.contrib.auth.forms import UserCreationForm
from Oddam_app.models import MyUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['password1','password2','email','first_name','last_name']
        labels = {'password1':'Hasło',
                  'password2':'Powtórz hasło',
                  'first_name':'Imię',
                  'last_name':'Nazwisko',
                  'email':'E-mail',
                  }

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