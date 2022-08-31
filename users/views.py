from django.shortcuts import render, redirect
from .models import Klient
from .forms import KlientForm
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
from django.db import models
from django.forms import ModelForm, TextInput, DateInput, NumberInput
import MySQLdb


def users_home(request):
    search_query = request.GET.get('search_user', '')

    if search_query:
        users = Klient.objects.filter(Phone__icontains=search_query)
    else:
        users = Klient.objects.all()
    users_count = Klient.objects.all().count()
    return render(request, 'users/users_home.html', {'users': users, 'users_count': users_count})

class UsersUpdateView(UpdateView):
    model = Klient
    fields = ['Phone', 'Name', 'Data_rozjden', 'Skidka']
    template_name = 'users/users_details_update.html'

    form = KlientForm

class UsersDeleteView(DeleteView):
    model = Klient
    success_url = '/users/'
    template_name = 'users/users_delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = KlientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_home')
        else:
            error = 'Неверно заполнены данные'
    form = KlientForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'users/users_create.html', data)
