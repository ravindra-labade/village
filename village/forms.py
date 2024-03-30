from django import forms
from .models import Village


class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = "__all__"

        widgets = {
            "village_name": forms.TextInput(attrs={'class': 'form-control'}),
            "tehsil": forms.TextInput(attrs={'class': 'form-control'}),
            "district": forms.TextInput(attrs={'class': 'form-control'}),
            "population": forms.NumberInput(attrs={'class': 'form-control'}),
            "village_head": forms.TextInput(attrs={'class': 'form-control'}),
        }
