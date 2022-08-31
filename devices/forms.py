from .models import Bron
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput, Select

class BronForm(ModelForm):
    class Meta:
        model = Bron
        fields = ['ID_Bron', 'Data_bron', 'Phone_bron', 'Name_bron', 'Komment', 'PC_ID_PC']

        widgets = {
            "Data_bron": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата бронирования'
            }),
            "Phone_bron": TextInput(attrs={
                'type': 'tel',
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "Name_bron": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "PC_ID_PC": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Номер ПК',
                'required': False,
            }),
            "Komment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
        }