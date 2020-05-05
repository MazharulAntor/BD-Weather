import requests
from django.shortcuts import render

from Information.models import City


def index(request):
    bd_url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=Metric&APPID=fa836872108421842ef8bdbdee0d6d0e'
    bd_r = requests.get(bd_url.format(1210997)).json()
    bd_weather = {
        'name': 'Bangladesh',
        'temperature': bd_r['main']['temp'],
        'description': bd_r['weather'][0]['description'],
        'icon': bd_r['weather'][0]['icon']
    }
    cities = City.objects.all()
    if request.method == "POST":
        city_id = int(request.POST.get('city_id'))

        url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=Metric&APPID=fa836872108421842ef8bdbdee0d6d0e'

        weather_data = []

        for city in cities:
            if city.city_id == city_id:
                r = requests.get(url.format(city_id)).json()

                weather = {
                    'name': city.name,
                    'temperature': r['main']['temp'],
                    'description': r['weather'][0]['description'],
                    'icon': r['weather'][0]['icon']
                }
                weather_data.append(weather)
                print(weather_data)

                context = {'weather_data': weather_data, 'cities': cities, 'bd_weather': bd_weather}
                return render(request, 'Information/weather.html', context)
    return render(request, 'Information/weather.html', {'cities': cities, 'bd_weather': bd_weather})
