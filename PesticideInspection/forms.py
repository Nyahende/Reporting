from django import forms
from .models import PesticideInspection

class PesticideInspectionForm(forms.ModelForm):
    class Meta:
        model = PesticideInspection
        fields = '__all__'
        
       
