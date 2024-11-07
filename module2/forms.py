from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    company = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))

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
        companies = kwargs.pop('companies', [])
        super().__init__(*args, **kwargs)
        self.fields['company'].choices = [(c['id'], c['name']) for c in companies]