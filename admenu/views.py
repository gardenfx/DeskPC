from django.shortcuts import render, redirect
from .models import Admin
from .forms import admininfoForm
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse


def admininfo_home(request):
    admininfo = Admin.objects.all();

    return render(request, 'admenu/admininfo_home.html', {'admininfo': admininfo})

class admininfoUpdateView(UpdateView):
    model = Admin
    template_name = 'admenu/admininfo_details_update.html'

    form_class = admininfoForm

class admininfoDeleteView(DeleteView):
    model = Admin
    success_url = '/admenu/'
    template_name = 'admenu/admininfo_delete.html'

def create_admininfo(request):
    error = ''
    if request.method == 'POST':
        form = admininfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admininfo_home')
        else:
            error = 'Неверно заполнены данные'

    form = admininfoForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'admenu/admininfo_create.html', data)