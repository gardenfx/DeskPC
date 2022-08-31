from django.shortcuts import render, redirect
from .models import vid_tovar, tovar
from .forms import ShopForm
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse


def shop_home(request):
    search_query = request.GET.get('search_shop', '')

    if search_query:
        shop = tovar.objects.filter(Nazv_tovar__icontains=search_query)
    else:
        shop = tovar.objects.all().order_by('Nazv_tovar');
        shop1 = vid_tovar.objects.all();

    return render(request, 'shop/shop_home.html', {'shop': shop, 'shop1': shop})

class ShopUpdateView(UpdateView):
    model = tovar
    model1 = vid_tovar
    template_name = 'shop/shop_details_update.html'

    form_class = ShopForm

class ShopDeleteView(DeleteView):
    model = tovar
    model1 = vid_tovar
    success_url = '/shop/'
    template_name = 'shop/shop_delete.html'

def create_shop(request):
    error = ''
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_home')
        else:
            error = 'Неверно заполнены данные'

    form = ShopForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'shop/shop_create.html', data)