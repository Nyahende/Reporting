from django import forms
from .models import PlantHealthInspection

class PlantHealthInspectionForm(forms.ModelForm):
    class Meta:
        model = PlantHealthInspection
        fields = '__all__'
        widgets = {
            'inspection_date': forms.DateInput(attrs={'type': 'date'}),
            'inspection_time': forms.TimeInput(attrs={'type': 'time'}),
            'follow_up_date': forms.DateInput(attrs={'type': 'date'}),
            'pests_diseases_detected': forms.Textarea(attrs={'rows': 3}),
            'immediate_actions': forms.Textarea(attrs={'rows': 3}),
            'recommendations': forms.Textarea(attrs={'rows': 3}),
            'challenges_encountered': forms.Textarea(attrs={'rows': 3}),
            'additional_notes': forms.Textarea(attrs={'rows': 3}),
            'recommendations_for_improvement': forms.Textarea(attrs={'rows': 3}),
        }
