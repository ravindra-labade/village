from django.shortcuts import render, redirect
from .forms import VillageForm
from .models import Village
from django.contrib.auth.decorators import login_required


def add_village(request):
    template_name = 'village/add.html'
    form = VillageForm()
    if request.method == 'POST':
        form = VillageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_village(request):
    template_name = 'village/show.html'
    villages = Village.objects.all()
    context = {'villages': villages}
    return render(request, template_name, context)


def update_village(request, pk):
    template_name = 'village/add.html'
    obj = Village.objects.get(id=pk)
    form = VillageForm(instance=obj)
    if request.method == 'POST':
        form = VillageForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def delete_village(request, pk):
    obj = Village.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'village/confirm.html')