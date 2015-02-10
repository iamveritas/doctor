# -*-coding:utf8-*-
from django import forms
from apps.internal.models import (Doctor, Hospital, Comment, CommentAnswer,
                                  Speciality, HospitalType, City,
                                  SEX_CHOICES, IS_STATE_CHOICES)

BOOTSTRAP_FORM_INPUT_CLASS = "form-control"


class DoctorForm(forms.ModelForm):

    last_name = forms.CharField(label="Прізвище", required=True,
                           widget=forms.TextInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть прізвище лікаря"
                           }))

    first_name = forms.CharField(label="Ім’я", required=True,
                           widget=forms.TextInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть ім’я лікаря"
                           }))

    patronymic = forms.CharField(label="По батькові", required=False,
                           widget=forms.TextInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть по батькові лікаря"
                           }))

    sex = forms.ChoiceField(choices=SEX_CHOICES, label="Стать", required=True,
                           widget=forms.Select(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                           }))

    speciality = forms.ModelChoiceField(queryset=Speciality.objects.all(), label="Спеціальність",
                           required=True, empty_label="Виберіть спеціальність",
                           widget=forms.Select(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                           }))

    hospitals = forms.ModelMultipleChoiceField(queryset=Hospital.objects.all(),label="Місце роботи", required=True,
                           widget=forms.SelectMultiple(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                           }))

    image = forms.ImageField(label="Фото", required=False)

    class Meta:
        model = Doctor
        fields = ['last_name', 'first_name', 'patronymic', 'sex', 'speciality', 'hospitals', 'image']


class HospitalForm(forms.ModelForm):

    name = forms.CharField(label="Назва клініки", required=True,
                           widget=forms.TextInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть назву клініки"
                           }))

    is_state = forms.ChoiceField(choices=IS_STATE_CHOICES, label="Державна", required=True,
                           widget=forms.Select(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                           }))

    type = forms.ModelChoiceField(queryset=HospitalType.objects.all(), label="Тип клініки",
                           required=True, empty_label="Оберіть тип клініки",
                           widget=forms.Select(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                           }))
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="Місто",
                           required=True, empty_label="Оберіть місто",
                           widget=forms.Select(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                           }))

    address = forms.CharField(label="Адреса (вулиця і номер будинку)", required=True,
                           widget=forms.TextInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть вулицю і будинок"
                           }))

    email = forms.EmailField(label="Email", required=False,
                           widget=forms.EmailInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть email"
                           }))

    phone = forms.CharField(label="Телефон", required=False,
                           widget=forms.TextInput(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Введіть телефон"
                           }))

    image = forms.ImageField(label="Фото", required=False)

    class Meta:
        model = Hospital
        fields = ['name', 'is_state', 'type', 'city', 'address', 'email', 'phone', 'image']


class CommentForm(forms.ModelForm):

    content = forms.CharField(required=True,
                           widget=forms.Textarea(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Що Ви можете сказати про цього лікаря?"
                           }))

    class Meta:
        model = Comment
        fields = ['content']


class CommentAnswerForm(forms.ModelForm):

    content = forms.CharField(required=True,
                           widget=forms.Textarea(attrs={
                               "class": BOOTSTRAP_FORM_INPUT_CLASS,
                               "placeholder": "Прокоментуйте відгук пацієнта?"
                           }))

    class Meta:
        model = CommentAnswer
        fields = ['content']
