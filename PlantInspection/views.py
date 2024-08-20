from django.shortcuts import render, redirect
from .models import PlantHealthInspection
from .forms import PlantHealthInspectionForm

def inspection_list(request):
    inspections = PlantHealthInspection.objects.all()
    return render(request, 'inspection_list.html', {'inspections': inspections})

def inspection_create(request):
    if request.method == 'POST':
        form = PlantHealthInspectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inspection_list')
    else:
        form = PlantHealthInspectionForm()
    return render(request, 'inspection_form.html', {'form': form})


def inspection_update(request, id):
    inspection = PlantHealthInspection.objects.get(id=id)
    if request.method == 'POST':
        form = PlantHealthInspectionForm(request.POST, instance=inspection)
        if form.is_valid():
            form.save()
            return redirect('inspection_list')
    else:
        form = PlantHealthInspectionForm(instance=inspection)
    return render(request, 'inspection_form.html', {'form': form})

def inspection_delete(request, id):
    inspection = PlantHealthInspection.objects.get(id=id)
    if request.method == 'POST':
        inspection.delete()
        return redirect('inspection_list')
    return render(request, 'inspection_confirm_delete.html', {'inspection': inspection})

from django.shortcuts import render, get_object_or_404

def inspection_detail(request, id):
    inspection = get_object_or_404(PlantHealthInspection, id=id)
    return render(request, 'inspection_detail.html', {'inspection': inspection})

