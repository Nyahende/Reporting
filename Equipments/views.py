from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipment
from .forms import EquipmentForm

def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'Equipments/equipment_list.html', {'equipment': equipment})

def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    return render(request, 'Equipments/equipment_detail.html', {'equipment': equipment})

def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'Equipments/equipment_form.html', {'form': form})

def equipment_update(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'Equipments/equipment_form.html', {'form': form})

def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')
    return render(request, 'Equipments/equipment_confirm_delete.html', {'equipment': equipment})
