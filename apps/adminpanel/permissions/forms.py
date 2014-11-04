from django import forms

from django.contrib.auth.models import Permission


class PermissionForm(forms.ModelForm):

    class Meta:
        model = Permission
        fields = ()