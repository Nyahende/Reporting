# reporting/models.py

from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    report = models.ForeignKey('MeetingReport', related_name='documents', on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name

class MeetingReport(models.Model):
    meeting_date = models.DateField()
    meeting_time_start = models.TimeField()
    meeting_time_end = models.TimeField()
    location = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    attendees = models.TextField()  # Store attendees as a list or comma-separated values

    agenda_items = models.TextField()
    presenter_lead = models.TextField()

    key_points_discussed = models.TextField()
    decisions_made = models.TextField()


    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} on {self.meeting_date}'
