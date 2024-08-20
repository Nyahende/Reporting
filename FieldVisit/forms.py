# field_visit/forms.py

from django import forms
from .models import FieldVisitReport



class FieldVisitReportForm(forms.ModelForm):
    class Meta:
        model = FieldVisitReport
        fields = '__all__'
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
            'visit_time_start': forms.TimeInput(attrs={'type': 'time'}),
            'visit_time_end': forms.TimeInput(attrs={'type': 'time'}),
            'purpose_of_visit': forms.Textarea(attrs={'rows': 2}),
            'site_description': forms.Textarea(attrs={'rows': 3}),
            'weather_conditions': forms.TextInput(attrs={'size': '50'}),
            'general_observations': forms.Textarea(attrs={'rows': 5}),
            'plant_health_status': forms.Textarea(attrs={'rows': 5}),
            'pest_activity': forms.Textarea(attrs={'rows': 5}),
            'soil_conditions': forms.Textarea(attrs={'rows': 5}),
            'infrastructure_condition': forms.Textarea(attrs={'rows': 5}),
            'problems_identified': forms.Textarea(attrs={'rows': 5}),
            'recommendations': forms.Textarea(attrs={'rows': 5}),
            'immediate_actions': forms.Textarea(attrs={'rows': 3}),
            'additional_notes': forms.Textarea(attrs={'rows': 3}),
            'challenges_encountered': forms.Textarea(attrs={'rows': 3}),
            'next_steps': forms.Textarea(attrs={'rows': 3}),
        }
