from .models import vid_tovar, tovar
from django import forms
from django.forms import ModelForm, NumberInput, TextInput, Select, ClearableFileInput


class ShopForm(ModelForm):
    class Meta:
        model = tovar
        fields = ['ID_tovar', 'Shtrih', 'Nazv_tovar', 'Cen_tovar', 'Vid_Tovar_ID_Vid']

        widgets = {
            "Shtrih": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Штрих-код',
                'type': 'number'
            }),
            "Nazv_tovar": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            "Cen_tovar": TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            }),
            'Vid_Tovar_ID_Vid': Select(attrs={
                'class': 'form-control',
            }),
        }
