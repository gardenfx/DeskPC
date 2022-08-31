from django.shortcuts import render, redirect
from .models import Oplat, Klient
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse
from users.models import Klient


def oplat_home(request):
    search_query = request.GET.get('search_oplat', '')

    if search_query:
        oplat = Oplat.objects.filter(Klient_ID_Klient__Phone__icontains=search_query)
    else:
        oplat = Oplat.objects.all();
        klient = Klient.objects.all();

    return render(request, 'oplat/oplat_home.html', {'oplat': oplat})