from django import forms
from .models import ZonalReport

class ZonalReportForm(forms.ModelForm):
    class Meta:
        model = ZonalReport
        fields = '__all__'
