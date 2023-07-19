from django import forms
from .models import *
from django.core.validators import ValidationError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['clients', 'rating', 'description']
        widgets = {
            'clients': forms.TextInput(attrs={'placeholder': 'Ваш ID номер..'}),
            'rating': forms.TextInput(attrs={'placeholder': 'Введите рейтинг от 0 до 5..'}),
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 6})
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating > 5:
            raise ValidationError('Введите рейтинг от 0 до 5')

        return rating

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) > 100:
            raise ValidationError('Длина отзыва превышает 100 символов')

        return description


class RegisterUserForm(UserCreationForm):
    username=forms.CharField(label='Ваш логин', widget=forms.TextInput(attrs={'placeholder': 'Логин..'}))
    email=forms.EmailField(label='Ваш email', widget=forms.TextInput(attrs={'placeholder': 'Введите Ваш email..'}))
    password1=forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'placeholder': 'Введите пароль..'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.TextInput(attrs={'placeholder': 'Повторите пароль..'}))
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Введите логин..'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль..'}))

