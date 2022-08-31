import datetime

from django.shortcuts import render, redirect
from .models import Opushen_tovar
from users.models import Klient
from shop.models import tovar, vid_tovar
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
from django.db import models
from urllib.parse import unquote
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import FileResponse
from decimal import Decimal
from rate.models import Kniga_ucheta
from django.db.models import Sum

def cashdesk_shop(request):
    search_query = request.GET.get('search_cashdesk_shop', '')

    if search_query:
        shop = tovar.objects.filter(Nazv_tovar__icontains=search_query)
    else:
        shop = tovar.objects.all();
        shop1 = vid_tovar.objects.all();

    infoprod = Kniga_ucheta.objects.all().order_by('-pk');
    sum_infoprod = sum(Kniga_ucheta.objects.values_list('Obsh_stoim', flat=True))

    return render(request, 'cashdesk/cashdesk_home.html', {'shop': shop, 'shop1': vid_tovar, 'infoprod': infoprod, 'sum_infoprod': sum_infoprod})


def addMoneyPhone(request):
    if request.method == 'GET':
        c = request.GET['cart']
        send_phone = request.GET['check_value']
        send_shop = request.GET['check_value1']
        j = json.loads(c)
        for item in j:
            try:
                if (send_phone == 'null'):
                    CreateRow_shop = Kniga_ucheta.objects.create(Nomer_chek=send_shop, Operac='Продажа', Obsh_stoim=float(item['price'].replace(',', '.')) * item['count'], Data_operac=item['time'])
                else:
                    pass
                if (float(item['price'].replace(',', '.')) > 0):
                    oper = 'Продажа'
                elif (float(item['price'].replace(',', '.')) < 0):
                    oper = 'Возврат'
                else:
                    pass
                if item['phone'] > '0':
                    for phone_db in Klient.objects.raw('''SELECT ID_Klient FROM Klient'''):
                        if item['phone'] == phone_db.Phone:
                            print('Номер найден')
                            phone_db.Balans = Decimal(int(item['price'])) + phone_db.Balans
                            phone_db.save()
                            if (send_shop == 'null'):
                                CreateRow_phone = Kniga_ucheta.objects.create(Nomer_chek=send_phone, Operac=oper, Obsh_stoim=float(item['price'].replace(',', '.'))*item['count'], Data_operac=item['time'])
                        else:
                            pass
            except KeyError as e:
                pass
    return render(request, 'cashdesk/cashdesk_home.html')

def venue_pdf(request):
    Kniga_ucheta_info = Kniga_ucheta.objects.all();
    sum_infoprod_print = sum(Kniga_ucheta.objects.values_list('Obsh_stoim', flat=True))
    infoprod_print = Kniga_ucheta.objects.all().order_by('-pk')
    Kniga_ucheta_info_count = Kniga_ucheta.objects.all().count
    back_count = 0
    shop_count = 0
    summa_shop = 0
    summa_back = 0
    now_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M') #'%d-%m-%Y %H:%M'
    for i in (Kniga_ucheta.objects.values_list('Obsh_stoim', flat=True)):
        try:
            if i < 0:
               back_count += 1
               summa_back += i
            if i > 0:
                shop_count += 1
                summa_shop += i
        except KeyError as e:
            pass
    return render(request, 'cashdesk/print.html', {'Kniga_ucheta_info': Kniga_ucheta_info, 'sum_infoprod_print': sum_infoprod_print, 'Kniga_ucheta_info_count': Kniga_ucheta_info_count,  'back_count':back_count, 'shop_count': shop_count, 'summa_shop': summa_shop, 'summa_back': summa_back, 'now_time': now_time})