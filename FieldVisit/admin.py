
from django.contrib import admin
from .models import FieldVisitReport

@admin.register(FieldVisitReport)
class FieldVisitReportAdmin(admin.ModelAdmin):
    list_display = ('visit_date', 'location', 'purpose_of_visit', 'visitors')
    search_fields = ('location', 'purpose_of_visit')




