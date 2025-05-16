import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import WeatherQuery
from .forms import WeatherQueryForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.core.cache import cache  #  импортируем cache

API_KEY = "f3245c4c35e5cf5a0d069850d0a238a9"


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def get_weather(request):
    weather_data = None

    if request.method == "POST":
        city = request.POST.get("city")
        cache_key = f"weather_{city}"

        # Пытаемся получить погоду из кэша
        weather_data = cache.get(cache_key)

        if not weather_data:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    "city": city,
                    "temp": round(data["main"]["temp"], 1),
                    "description": data["weather"][0]["description"],
                }
                # Сохраняем данные в кэш на 60 секунд
                cache.set(cache_key, weather_data, 60)

                # Сохраняем в базу данных
                WeatherQuery.objects.create(
                    city=weather_data["city"],
                    temperature=weather_data["temp"],
                    description=weather_data["description"]
                )

    return render(request, "main/home.html", {"weather": weather_data})


def weather_history(request):
    history = WeatherQuery.objects.order_by('-date_checked')
    return render(request, "weather/history.html", {"history": history})


def weather_list(request):
    weather_data = WeatherQuery.objects.all()
    return render(request, 'weather/weather_list.html', {'weather_data': weather_data})


def weather_create(request):
    if request.method == 'POST':
        form = WeatherQueryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weather_list')
    else:
        form = WeatherQueryForm()
    return render(request, 'weather/weather_form.html', {'form': form})


def weather_update(request, pk):
    weather = get_object_or_404(WeatherQuery, pk=pk)
    if request.method == 'POST':
        form = WeatherQueryForm(request.POST, instance=weather)
        if form.is_valid():
            form.save()
            return redirect('weather_list')
    else:
        form = WeatherQueryForm(instance=weather)
    return render(request, 'weather/weather_form.html', {'form': form})


def weather_delete(request, pk):
    weather = get_object_or_404(WeatherQuery, pk=pk)
    if request.method == 'POST':
        weather.delete()
        return redirect('weather_list')
    return render(request, 'weather/weather_confirm_delete.html', {'weather': weather})
