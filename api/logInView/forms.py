from django.forms import ModelForm
from api.signUpView.models import Profile
from django import forms


class LoginForm(ModelForm):
    username = forms.CharField(label="Потребителско име", max_length=64,
                               widget=forms.TextInput(attrs={'class': 'input mr',
                                                             'placeholder': 'Mitko123'}))
    password = forms.CharField(label='Парола', max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'input mr',
                                                                 'placeholder': '********'}))

    class Meta:
        model = Profile
        fields = ['username', 'password']
