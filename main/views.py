from django.shortcuts import render


def index(request):
    data={
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123']
    }
    return render(request, 'main/index.html', data)

def mapgrid(request):
    return render(request, 'main/mapgrid.html')

def cashdesk(request):
    return render(request, 'main/cashdesk.html')

def shop(request):
    return render(request, 'main/shop.html')

def devices(request):
    return render(request, 'main/devices.html')

def content(request):
    return render(request, 'main/content.html')

def rate(request):
    return render(request, 'main/rate.html')

def admenu(request):
    return render(request, 'main/admenu.html')

def auth(request):
    return render(request, 'main/auth.html')

def users(request):
    return render(request, 'main/users.html')