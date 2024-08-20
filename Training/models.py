from django.db import models
from django.utils import timezone

class Training(models.Model):
    TRAINING_TYPES = [
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar'),
        ('field_demonstration', 'Field Demonstration'),
    ]
    
    TARGET_AUDIENCES = [
        ('farmers', 'Farmers'),
        ('extension_officers', 'Extension Officers'),
        ('stakeholders', 'Stakeholders'),
        ('workers', 'Workers'),
    ]
    
    # General Information
    training_date = models.DateField(default=timezone.now)
    training_start_time = models.TimeField()
    training_end_time = models.TimeField()
    trainer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    training_type = models.CharField(max_length=50, choices=TRAINING_TYPES)
    target_audience = models.CharField(max_length=50, choices=TARGET_AUDIENCES)

    # Training Content
    training_topics = models.TextField()
    training_methods = models.TextField()

    # Training Outcomes
    skills_knowledge_gained = models.TextField()
    assessments_conducted = models.TextField()
    participant_feedback = models.TextField()

    # Training Effectiveness
    training_impact = models.TextField()

    # Additional Observations
    additional_notes = models.TextField(blank=True)
    challenges_encountered = models.TextField(blank=True)
    recommendations = models.TextField(blank=True)

    def __str__(self):
        return f"Training on {self.training_date} at {self.location}"
