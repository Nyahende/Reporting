# reporting/views.py

from django.shortcuts import render, redirect
from .models import MeetingReport, Document
from .forms import MeetingReportForm, DocumentFormSet
from django.shortcuts import render, get_object_or_404, redirect


def meeting_report_list(request):
    reports = MeetingReport.objects.all()
    return render(request, 'Meetings/meeting_report_list.html', {'reports': reports})

def meeting_report_create(request):
    if request.method == 'POST':
        form = MeetingReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            formset = DocumentFormSet(request.POST, request.FILES, instance=report)
            if formset.is_valid():
                formset.save()
                return redirect('meeting_report_list')
    else:
        form = MeetingReportForm()
        formset = DocumentFormSet()

    return render(request, 'Meetings/meeting_report_form.html', {'form': form, 'formset': formset})

def update_meeting_report(request, pk):
    report = get_object_or_404(MeetingReport, pk=pk)
    if request.method == 'POST':
        form = MeetingReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('meeting_report_detail', pk=report.pk)
    else:
        form = MeetingReportForm(instance=report)
    return render(request, 'Meetings/update_meeting_report.html', {'form': form})

def meeting_report_detail(request, pk):
    report = MeetingReport.objects.get(pk=pk)
    documents = report.documents.all()
    return render(request, 'Meetings/meeting_report_detail.html', {'report': report, 'documents': documents})


def delete_meeting_report(request, pk):
    report = get_object_or_404(MeetingReport, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('meeting_report_list')
    return render(request, 'Meetings/delete_meeting_report.html', {'report': report})


