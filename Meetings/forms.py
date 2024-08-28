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
            'agenda_items': forms.Textarea(attrs={'rows': 2}),
            'attendees': forms.Textarea(attrs={'rows': 2}),
            'presenter_lead': forms.Textarea(attrs={'rows': 2}),
            'key_points_discussed': forms.Textarea(attrs={'rows': 2}),
            'decisions_made': forms.Textarea(attrs={'rows': 2}),
            'additional_notes': forms.Textarea(attrs={'rows': 2}),
        }

DocumentFormSet = inlineformset_factory(MeetingReport, Document, form=DocumentForm, extra=1, can_delete=False)
