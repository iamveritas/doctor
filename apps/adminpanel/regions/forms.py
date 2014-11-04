from django import forms

from apps.internal.models import Region


class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = ()