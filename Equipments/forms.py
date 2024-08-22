from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'make': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'purpose': forms.Textarea(attrs={'class': 'form-control'}),
            'frequency_of_use': forms.TextInput(attrs={'class': 'form-control'}),
            'users': forms.TextInput(attrs={'class': 'form-control'}),
            'training_records': forms.Textarea(attrs={'class': 'form-control'}),
            'condition': forms.TextInput(attrs={'class': 'form-control'}),
            'performance': forms.Textarea(attrs={'class': 'form-control'}),
            'capacity': forms.Textarea(attrs={'class': 'form-control'}),
            'compliance': forms.Textarea(attrs={'class': 'form-control'}),
            'routine_maintenance': forms.Textarea(attrs={'class': 'form-control'}),
            'preventive_maintenance': forms.Textarea(attrs={'class': 'form-control'}),
            'corrective_maintenance': forms.Textarea(attrs={'class': 'form-control'}),
            'service_contracts': forms.Textarea(attrs={'class': 'form-control'}),
            'maintenance_logs': forms.Textarea(attrs={'class': 'form-control'}),
            'calibration_records': forms.Textarea(attrs={'class': 'form-control'}),
            'inspection_reports': forms.Textarea(attrs={'class': 'form-control'}),
            'repair_records': forms.Textarea(attrs={'class': 'form-control'}),
            'regulatory_compliance': forms.Textarea(attrs={'class': 'form-control'}),
            'manufacturer_guidelines': forms.Textarea(attrs={'class': 'form-control'}),
            'performance_metrics': forms.Textarea(attrs={'class': 'form-control'}),
            'downtime_records': forms.Textarea(attrs={'class': 'form-control'}),
            'upgrade_recommendations': forms.Textarea(attrs={'class': 'form-control'}),
            'training_needs': forms.Textarea(attrs={'class': 'form-control'}),
            'risk_factors': forms.Textarea(attrs={'class': 'form-control'}),
            'mitigation_measures': forms.Textarea(attrs={'class': 'form-control'}),
            'maintenance_costs': forms.NumberInput(attrs={'class': 'form-control'}),
            'budget_allocation': forms.NumberInput(attrs={'class': 'form-control'}),
        }
