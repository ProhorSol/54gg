from .models import Staff
from django.forms import ModelForm, TextInput, EmailInput, Select

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ["name", "number", "mail", "ph_number", "jb"]
        widgets ={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванов Иван Иванович'
                }),"number": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': '1'
                    }),"mail": EmailInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'foma@gmail.com'
                        }),"ph_number": TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': '89054325517'
                            }),'jb': Select(attrs={
                                'class': 'form-control'})
                        }