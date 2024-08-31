
from django.shortcuts import render, redirect
from .models import FieldVisitReport
from .forms import FieldVisitReportForm
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

def field_visit_report_list(request):
    reports = FieldVisitReport.objects.all()
    return render(request, 'FieldVisit/field_visit_report_list.html', {'reports': reports})

def field_visit_report_create(request):
    if request.method == 'POST':
        form = FieldVisitReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            return redirect('field_visit_report_list')
    else:
        form = FieldVisitReportForm()
    return render(request, 'FieldVisit/field_visit_report_form.html', {'form': form})

def field_visit_report_detail(request, pk):
    report = FieldVisitReport.objects.get(pk=pk)
    return render(request, 'FieldVisit/field_visit_report_detail.html', {'report': report})

def delete_field_visit(request, pk):
    visit = get_object_or_404(FieldVisitReport, pk=pk)
    if request.method == 'POST':
        visit.delete()
        return redirect('field_visit_list')
    return render(request, 'FieldVisit/delete_field_visit.html', {'visit': visit})

def update_field_visit(request, pk):
    visit = get_object_or_404(FieldVisitReport, pk=pk)
    if request.method == 'POST':
        form = FieldVisitReportForm(request.POST, request.FILES, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('field_visit_report_detail', pk=visit.pk)
    else:
        form = FieldVisitReportForm(instance=visit)
    return render(request, 'FieldVisit/field_visit_report_form.html', {'form': form, 'visit': visit})

