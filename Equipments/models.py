from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    purpose = models.TextField()
    frequency_of_use = models.CharField(max_length=255)
    users = models.CharField(max_length=255)
    training_records = models.TextField()
    condition = models.CharField(max_length=255)
    performance = models.TextField()
    capacity = models.TextField()
    compliance = models.TextField()
    routine_maintenance = models.TextField()
    preventive_maintenance = models.TextField()
    corrective_maintenance = models.TextField()
    service_contracts = models.TextField()
    maintenance_logs = models.TextField()
    calibration_records = models.TextField()
    inspection_reports = models.TextField()
    repair_records = models.TextField()
    regulatory_compliance = models.TextField()
    manufacturer_guidelines = models.TextField()
    performance_metrics = models.TextField()
    downtime_records = models.TextField()
    upgrade_recommendations = models.TextField()
    training_needs = models.TextField()
    risk_factors = models.TextField()
    mitigation_measures = models.TextField()
    maintenance_costs = models.DecimalField(max_digits=10, decimal_places=2)
    budget_allocation = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
