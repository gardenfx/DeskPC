from .models import PC
from django.forms import ModelForm, TextInput, NumberInput, Select

class PCform(ModelForm):
    class Meta:
        model = PC
        fields = ['ID_PC', 'Number', 'Status', 'Stoim']

        widgets = {
            "Number": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер компьютера'
            }),
                "Status": Select(attrs={
               'class': 'form-control'
                }
            ),
            "Stoim": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость'
            }),
        }
