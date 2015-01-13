#-*-coding:utf8-*-
from django import forms
from apps.accounts.models import UserDoctor
from apps.internal.models import Doctor

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField

BOOTSTRAP_FORM_INPUT_CLASS = "form-control"


class UserForm(UserCreationForm):

    username = forms.RegexField(label=_("Username"), max_length=30, regex=r'^[\w.@+-]+$',
                                widget=forms.TextInput(attrs={
                                    "class": BOOTSTRAP_FORM_INPUT_CLASS,
                                    "placeholder": "Введіть логін",
                                }))
    email = forms.EmailField(label=_("Email"),
                           widget=forms.EmailInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть email",
                           }))
    password1 = forms.CharField(label=_("Password"), required=True,
                           widget=forms.PasswordInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть пароль",
                           }))
    password2 = forms.CharField(label=_("Password confirmation"), required=True,
                           widget=forms.PasswordInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть пароль ще раз",
                           }))

    rules = forms.BooleanField(label="Умови використання", required=True)

    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'rules', 'captcha')


class LoginForm(forms.Form):

    username = forms.CharField(label="Логін", required=True,
                           widget=forms.TextInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть логін"
                           }))
    password = forms.CharField(label=_("Password"), required=True,
                           widget=forms.PasswordInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть пароль",
                           }))

    class Meta:
        fields = ('username', 'password')


class UserDoctorForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label="Виберіть себе серед лікарів",
                           required=True,
                           widget=forms.Select(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                           }))
    class Meta:
        model = UserDoctor
        fields = ['doctor']
