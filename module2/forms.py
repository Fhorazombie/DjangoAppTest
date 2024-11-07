from django import forms
from .models import Client
from module1.models import Company

class ClientForm(forms.ModelForm):
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address', 'company']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        companies = kwargs.pop('companies', None)
        super().__init__(*args, **kwargs)
        if companies is not None:
            # Si `companies` se pasa, utiliza el queryset proporcionado
            self.fields['company'].queryset = companies
