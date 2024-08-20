from django.db import models
from django.utils import timezone

class PesticideInspection(models.Model):
    # General Information
    inspection_date = models.DateField(default=timezone.now)
    inspection_time = models.TimeField(default=timezone.now)
    location = models.CharField(max_length=255)
    inspector_name = models.CharField(max_length=100)

    # Seller Details
    seller_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    license_expiry_date = models.DateField()
    contact_information = models.CharField(max_length=255)

    # Inventory Inspection
    product_list = models.TextField()

    

    # Inspection Findings
    violations_detected = models.TextField(blank=True)
    non_compliant_products = models.TextField(blank=True)
    corrective_actions_required = models.TextField(blank=True)
    follow_up_inspection_needed = models.BooleanField(default=False)
    follow_up_date = models.DateField(null=True, blank=True)

    # Actions Taken
    penalties_issued = models.TextField(blank=True)

    # Supporting Documents
    photographic_evidence = models.ImageField(upload_to='inspection_photos/', blank=True, null=True)
    

    # Additional Observations
    challenges_encountered = models.TextField(blank=True)
    additional_notes = models.TextField(blank=True)
    recommendations_for_improvement = models.TextField(blank=True)

    def __str__(self):
        return f"Inspection on {self.inspection_date} at {self.location}"
