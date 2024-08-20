from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ZonalReport(models.Model):
    STATIONS = [
        ('mtwara', 'Mtwara'), ('mtambaswala', 'Mtambaswala'), ('kasesya', 'Kasesya'),
        ('kirando', 'Kirando'), ('kabwe', 'Kabwe'), ('karema', 'Karema'),
        ('manyovu', 'Manyovu'), ('kibirizi', 'Kibirizi'), ('kigoma', 'Kigoma'),
        ('mabamba', 'Mabamba'), ('mwanza', 'Mwanza'), ('sirari', 'Sirari'),
        ('kabanga', 'Kabanga'), ('musoma', 'Musoma'), ('rusumo', 'Rusumo'),
        ('mutukula', 'Mutukula'), ('bukoba', 'Bukoba'), ('murusagamba', 'Murusagamba'),
        ('murongo', 'Murongo'), ('bukoba_airport', 'Bukoba Airport'), ('jnia', 'JNIA'),
        ('kurasini', 'Kurasini'), ('tanga', 'Tanga'), ('horohoro', 'Horohoro'),
        ('bagamoyo', 'Bagamoyo'), ('kwala', 'Kwala'), ('holili', 'Holili'),
        ('tarakea', 'Tarakea'), ('kia', 'KIA'), ('tengeru', 'Tengeru'), 
        ('namanga', 'Namanga')
    ]
    
    # General Information
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    station = models.CharField(max_length=50, choices=STATIONS)
    
    # Inspector Information
    number_of_inspectors = models.PositiveIntegerField()

    # Export Certification
    plant_consignments_certified = models.PositiveIntegerField()
    phytosanitary_certificates_issued = models.PositiveIntegerField()
    consignments_not_meeting_export_requirements = models.PositiveIntegerField()
    export_non_compliance_measures = models.TextField()

    # Import Certification
    plant_import_permits_issued = models.PositiveIntegerField()
    imported_plant_consignments_verified = models.PositiveIntegerField()
    imported_consignments_on_transit = models.PositiveIntegerField()
    consignments_not_meeting_import_requirements = models.PositiveIntegerField()
    import_non_compliance_measures = models.TextField()
    import_challenges = models.TextField(blank=True)

    # Pesticide Inspection
    pesticides_consignments_received_inspected = models.PositiveIntegerField()
    pesticides_consignments_not_meeting_requirements = models.PositiveIntegerField()
    pesticide_non_compliance_measures = models.TextField()
    pesticide_challenges = models.TextField(blank=True)

    # Field Visits & Surveillance
    field_visits = models.PositiveIntegerField()
    surveillance_work = models.TextField()
    key_pests_diseases_observed = models.TextField()
    geographical_coverage_of_pests = models.TextField()
    preliminary_measures_taken = models.TextField()

    # Crop Inspection
    fields_crops_inspected = models.PositiveIntegerField()
    crop_non_compliance_observed = models.TextField()
    crop_non_compliance_measures = models.TextField()

    # Pesticide Business Inspections
    pesticide_businesses_inspected = models.PositiveIntegerField()
    pesticide_business_non_compliance = models.TextField(blank=True)

    # Stakeholder Engagement
    stakeholder_groups_met = models.PositiveIntegerField()
    stakeholder_concerns = models.TextField()

    # Field Work & Community Meetings
    other_field_work_activities = models.TextField()
    community_meetings_attended = models.TextField()
    community_concerns = models.TextField()

    # On-call Attendances
    on_call_plant_health = models.TextField(blank=True)
    on_call_pesticide_management = models.TextField(blank=True)

    # Additional Information
    other_important_matters = models.TextField(blank=True)

    def __str__(self):
        return f"{self.station} - {self.date}"
