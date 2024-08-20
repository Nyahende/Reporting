from .models import Training
from .forms import TrainingForm
from django.shortcuts import get_object_or_404, redirect, render


def training_update(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == 'POST':
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm(instance=training)
    return render(request, 'Training/training_form.html', {'form': form})



def training_delete(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == 'POST':
        training.delete()
        return redirect('training_list')
    return render(request, 'Training/training_confirm_delete.html', {'training': training})



def training_create(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm()
    return render(request, 'Training/training_form.html', {'form': form})

def training_list(request):
    trainings = Training.objects.all()
    return render(request, 'Training/training_list.html', {'trainings': trainings})

def training_detail(request, pk):
    training = Training.objects.get(pk=pk)
    return render(request, 'Training/training_detail.html', {'training': training})
