from django.shortcuts import render
from .Utility import *

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        if CheckCityName(city):
            x = get_weather(city)
            context = {'city': city,
                       'temperature': x['temperature'],
                       'country': x['country'],
                       'time': x['time'],
                       }
            return render(request, 'base.html', context)
        else:
            return render(request, 'base.html', {'cityname_Valid': False})
    else:
        return render(request, 'base.html')
