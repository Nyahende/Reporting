from django.shortcuts import render, get_object_or_404, redirect
from .models import ZonalReport
from .forms import ZonalReportForm
from django.http import HttpResponse
from django.template.loader import get_template
# from weasyprint import HTML
import xlsxwriter
import io
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd

def zonal_report_create(request):
    if request.method == 'POST':
        form = ZonalReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('zonal_report_list')
    else:
        form = ZonalReportForm()
    return render(request, 'ZonalReports/zonal_report_form.html', {'form': form})

def zonal_report_list(request):
    reports = ZonalReport.objects.all()
    return render(request, 'ZonalReports/zonal_report_list.html', {'reports': reports})

def zonal_report_detail(request, pk):
    report = get_object_or_404(ZonalReport, pk=pk)
    return render(request, 'ZonalReports/zonal_report_detail.html', {'report': report})

def zonal_report_filter(request):
    filter_type = request.GET.get('filter', 'daily')
    today = datetime.today().date()

    if filter_type == 'weekly':
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)
    elif filter_type == 'monthly':
        start_date = today.replace(day=1)
        end_date = (today.replace(month=today.month+1, day=1) - timedelta(days=1))
    elif filter_type == 'yearly':
        start_date = today.replace(month=1, day=1)
        end_date = today.replace(month=12, day=31)
    else:
        start_date = today
        end_date = today

    reports = ZonalReport.objects.filter(date__range=[start_date, end_date])
    return render(request, 'ZonalReports/zonal_report_list.html', {'reports': reports, 'filter_type': filter_type})




from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

def zonal_report_update(request, pk):
    report = get_object_or_404(ZonalReport, pk=pk)
    if request.user != report.created_by:
        return HttpResponseForbidden("You are not allowed to edit this report.")
    
    if request.method == 'POST':
        form = ZonalReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('zonal_report_list')
    else:
        form = ZonalReportForm(instance=report)
    
    return render(request, 'ZonalReports/zonal_report_form.html', {'form': form})


def zonal_report_delete(request, pk):
    report = get_object_or_404(ZonalReport, pk=pk)
    if request.user != report.created_by:
        return HttpResponseForbidden("You are not allowed to delete this report.")
    
    if request.method == 'POST':
        report.delete()
        return redirect('zonal_report_list')
    
    return render(request, 'ZonalReports/zonal_report_confirm_delete.html', {'report': report})

