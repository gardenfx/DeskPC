from .models import Admin
from django.forms import ModelForm, TextInput, DateInput, NumberInput, Select

class admininfoForm(ModelForm):
    class Meta:
        model = Admin
        fields = ['ID_admin', 'FIO']

        widgets = {
            "ID_admin": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID админ'
            }),
            "FIO": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            }