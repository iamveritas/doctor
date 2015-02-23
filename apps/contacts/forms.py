#-*-coding:utf8-*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from captcha.fields import CaptchaField

BOOTSTRAP_FORM_INPUT_CLASS = "form-control"


class FeedbackForm(forms.Form):

    name = forms.CharField(label=_("Your Name"), required=True,
                           widget=forms.TextInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Ваше ім’я"
                           }))
    email = forms.EmailField(label=_("Email"), required=True,
                             widget=forms.TextInput(attrs={
                                 "class": BOOTSTRAP_FORM_INPUT_CLASS,
                                 "placeholder": "Email"
                             }))
    text = forms.CharField(label=_("Message or Question"), required=True,
                           widget=forms.Textarea({
                               "cols": 5,
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Ваше повідомлення"
                           }))
    captcha = CaptchaField()

    class Meta:
        fields = ('name', 'email', 'text', 'captcha')