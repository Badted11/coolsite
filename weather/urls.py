from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page

from weather import views as weather_views
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    # Главная страница погоды с кэшированием на 60 секунд
    path('', cache_page(60)(weather_views.get_weather), name='weather'),

    # История прогнозов
    path('history/', weather_views.weather_history, name='history'),

    # Аутентификация
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', weather_views.register, name='register'),

    # CRUD погоды
    path('list/', weather_views.weather_list, name='weather_list'),
    path('add/', weather_views.weather_create, name='weather_create'),
    path('edit/<int:pk>/', weather_views.weather_update, name='weather_update'),
    path('delete/<int:pk>/', weather_views.weather_delete, name='weather_delete'),

    # Панель администратора
    path('admin/', admin.site.urls),
]

# Debug toolbar
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

# Для отображения загруженных изображений (media)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
