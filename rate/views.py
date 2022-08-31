from django.shortcuts import render, redirect
from .models import Kniga_ucheta, Smen
from admenu.models import Admin
from users.models import Klient
from devices.models import PC
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse


def kniga_ucheta_home(request):
        search_query = request.GET.get('search_knig', '')

        if search_query:
                knig_uchet = Kniga_ucheta.objects.filter(Admin_ID_admin__kniga_ucheta__Nomer_chek__icontains=search_query);
                smen = Smen.objects.all();
                adpanel = Admin.objects.all();
                klient = Klient.objects.all();
                pc = PC.objects.all();
        else:
                knig_uchet = Kniga_ucheta.objects.all();
                smen = Smen.objects.all();
                adpanel = Admin.objects.all();
                klient = Klient.objects.all();
                pc = PC.objects.all();

        return render(request, 'rate/rate_home.html', {'knig_uchet': knig_uchet, 'smen': smen, 'adpanel': adpanel, 'klient': klient, 'pc': pc})