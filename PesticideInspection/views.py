from django.shortcuts import render, get_object_or_404, redirect
from .models import PesticideInspection
from .forms import PesticideInspectionForm

def pesticide_inspection_list(request):
    inspections = PesticideInspection.objects.all()
    return render(request, 'PesticideInspection/pesticide_inspection_list.html', {'inspections': inspections})

def pesticide_inspection_detail(request, id):
    inspection = get_object_or_404(PesticideInspection, id=id)
    return render(request, 'PesticideInspection/pesticide_inspection_detail.html', {'inspection': inspection})

def pesticide_inspection_create(request):
    if request.method == 'POST':
        form = PesticideInspectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pesticide_inspection_list')
        else:
            print(form.errors)
    else:
        form = PesticideInspectionForm()
    return render(request, 'PesticideInspection/pesticide_inspection_form.html', {'form': form})

def pesticide_inspection_update(request, id):
    inspection = get_object_or_404(PesticideInspection, id=id)
    if request.method == 'POST':
        form = PesticideInspectionForm(request.POST, request.FILES, instance=inspection)
        if form.is_valid():
            form.save()
            return redirect('pesticide_inspection_detail', id=inspection.id)
    else:
        form = PesticideInspectionForm(instance=inspection)
    return render(request, 'PesticideInspection/pesticide_inspection_form.html', {'form': form})

def pesticide_inspection_delete(request, id):
    inspection = get_object_or_404(PesticideInspection, id=id)
    if request.method == 'POST':
        inspection.delete()
        return redirect('pesticide_inspection_list')
    return render(request, 'PesticideInspection/pesticide_inspection_confirm_delete.html', {'inspection': inspection})
