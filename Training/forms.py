from django import forms
from .models import Training

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'  # Include all fields from the model
        widgets = {
            'training_date': forms.DateInput(attrs={'type': 'date'}),
            'training_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'training_end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
