from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),              # Админка Django
    path('', include('main.urls')),               # Основное приложение
    path('weather/', include('weather.urls')),    # Приложение с погодой
]
