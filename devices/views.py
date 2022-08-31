from django.shortcuts import render, redirect
from .models import Bron
from .forms import BronForm
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse
from mapgrid.models import PC


def bron_home(request):
    search_query = request.GET.get('search_bron', '')
    if search_query:
        reserve = Bron.objects.filter(Name_bron__icontains=search_query)
    else:
        reserve = Bron.objects.all();
        bron_check = ", ".join(PC.objects.filter(Status='Свободен').values_list('Number', flat=True));

    return render(request, 'devices/devices_home.html', {'reserve': reserve, 'bron_check': bron_check})

class BronUpdateView(UpdateView):
    model = Bron
    template_name = 'devices/devices_details_update.html'
    form_class = BronForm

class BronDeleteView(DeleteView):
    model = Bron
    success_url = '/devices/'
    template_name = 'devices/devices_delete.html'

def create_bron(request):
    bron_check = ", ".join(PC.objects.filter(Status='Свободен').values_list('Number', flat=True));
    error = ''
    if request.method == 'POST':
        form = BronForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bron_home')
        else:
            error = 'Неверно заполнены данные'

    form = BronForm()

    data = {
        'form': form,
        'error': error,
        'bron_check': bron_check
    }

    return render(request, 'devices/devices_create.html', data)
