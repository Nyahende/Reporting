

from django.db import models

class FieldVisitReport(models.Model):
    visit_date = models.DateField()
    visit_time_start = models.TimeField()
    visit_time_end = models.TimeField()
    location = models.CharField(max_length=255)
    purpose_of_visit = models.TextField()
    visitors = models.CharField(max_length=255)
    field_contact_person = models.CharField(max_length=255)
    field_contact_person_phone = models.CharField(max_length=20, blank=True, null=True)

    site_description = models.TextField()
    weather_conditions = models.CharField(max_length=255)

    general_observations = models.TextField()
    plant_health_status = models.TextField()
    pest_activity = models.TextField()
    soil_conditions = models.TextField()
    infrastructure_condition = models.TextField()

    problems_identified = models.TextField()
    recommendations = models.TextField()

    immediate_actions = models.TextField()


    additional_notes = models.TextField(blank=True, null=True)
    challenges_encountered = models.TextField(blank=True, null=True)
    next_steps = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Field Visit Report on {self.visit_date}'

