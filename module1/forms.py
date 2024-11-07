from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'phone_number', 'email', 'website', 'industry', 'founded_date']
        widgets = {

            'founded_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
                'type': 'date',  # Tipo de input para seleccionar fecha
            }),
        }