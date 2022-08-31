from .models import Klient
from django.forms import ModelForm, TextInput, DateInput, NumberInput

class KlientForm(ModelForm):
    class Meta:
        model = Klient
        fields = ['ID_Klient', 'Phone', 'Name', 'Data_rozjden', 'Skidka', 'Balans']

        widgets = {
            "Phone": NumberInput(attrs={
                'type': 'tel',
                'type': 'number',
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "Data_rozjden": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            }),
            "Skidka": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Скидка'
            }),
            "Balans": TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }),
        }