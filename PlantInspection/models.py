from django.db import models
from django.utils import timezone

class PlantHealthInspection(models.Model):
    INSPECTION_LOCATIONS = [
        ('tunduma', 'Tunduma'),
        ('kasumulu', 'Kasumulu'),
        ('songwe', 'Songwe'),
    ]
    
    # General Information
    inspection_date = models.DateField(default=timezone.now)
    inspection_time = models.TimeField(default=timezone.now)
    location = models.CharField(max_length=50, choices=INSPECTION_LOCATIONS)
    inspector_name = models.CharField(max_length=100)

    # Details of Inspected Items
    item_description = models.CharField(max_length=200)
    origin = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    condition_of_items = models.CharField(max_length=100)

    # Inspection Findings
    pests_diseases_detected = models.TextField(blank=True)
    laboratory_analysis_required = models.BooleanField(default=False)
    sample_collected = models.BooleanField(default=False)
    quarantine_required = models.BooleanField(default=False)
    items_seized = models.BooleanField(default=False)

    # Actions Taken
    immediate_actions = models.TextField(blank=True)
    follow_up_required = models.BooleanField(default=False)
    follow_up_date = models.DateField(null=True, blank=True)
    
    # Additional Observations
    challenges_encountered = models.TextField(blank=True)
    additional_notes = models.TextField(blank=True)
    recommendations_for_improvement = models.TextField(blank=True)

    def __str__(self):
        return f"Inspection on {self.inspection_date} at {self.location}"

