from django.shortcuts import render, redirect
from .models import PC
from .forms import PCform
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse


def PC_home(request):
    PCout = PC.objects.all()
    PCount = PC.objects.all().count
    PCfilterCheckFree = PC.objects.filter(Status='Свободен').count
    PCfilterCheckNofree = PC.objects.filter(Status='Занят').count
    PCfilterObsl = PC.objects.filter(Status='В обслуживании').count
    PCfilterBron = PC.objects.filter(Status='Забронирован').count
    return render(request, 'PC/map_grid_home.html', {'PC': PCout, 'PCcount': PCount, 'PCfilterCheckFree': PCfilterCheckFree, 'PCfilterCheckNofree': PCfilterCheckNofree, 'PCfilterObsl': PCfilterObsl, 'PCfilterBron': PCfilterBron})

class PCUpdateView(UpdateView):
    model = PC
    template_name = 'PC/PC_details_update.html'
    form_class = PCform

class PCDeleteView(DeleteView):
    model = PC
    success_url = '/map-grid/'
    template_name = 'PC/PC_delete.html'

def addPC(request):
    error = ''
    if request.method == 'POST':
        form_PC = PCform(request.POST)
        if form_PC.is_valid():
            form_PC.save()
            return redirect('map_grid')
        else:
            error = 'Неверно заполнены данные'

    form_PC = PCform()

    data = {
        'form': form_PC,
        'error': error
    }

    return render(request, 'PC/PC_create.html', data)
