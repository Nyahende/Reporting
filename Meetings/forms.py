# reporting/forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import MeetingReport, Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']

class MeetingReportForm(forms.ModelForm):
    class Meta:
        model = MeetingReport
        fields = '__all__'
        widgets = {
            'meeting_date': forms.DateInput(attrs={'type': 'date'}),
            'meeting_time_start': forms.TimeInput(attrs={'type': 'time'}),
            'meeting_time_end': forms.TimeInput(attrs={'type': 'time'}),
            'agenda_items': forms.Textarea(attrs={'rows': 3}),
            'presenter_lead': forms.Textarea(attrs={'rows': 3}),
            'key_points_discussed': forms.Textarea(attrs={'rows': 5}),
            'decisions_made': forms.Textarea(attrs={'rows': 5}),
            'additional_notes': forms.Textarea(attrs={'rows': 3}),
        }

DocumentFormSet = inlineformset_factory(MeetingReport, Document, form=DocumentForm, extra=1, can_delete=False)
