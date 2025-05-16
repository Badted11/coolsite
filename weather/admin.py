from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import FavoriteCity, WeatherQuery

# Кастомизация панели
admin.site.site_title = "Админка Погоды"
admin.site.site_header = "Управление погодным сервисом"

@admin.register(FavoriteCity)
class FavoriteCityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'user', 'added_at')
    search_fields = ('city_name', 'user__username')

@admin.register(WeatherQuery)
class WeatherQueryAdmin(admin.ModelAdmin):
    list_display = ('city', 'temperature', 'description', 'date_checked', 'get_html_photo')
    search_fields = ('city',)
    list_filter = ('date_checked',)

    # Только существующие поля!
    readonly_fields = ('get_html_photo', 'date_checked')
    fields = ('city', 'temperature', 'description', 'photo', 'get_html_photo', 'date_checked')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width='50'>")
        return "Нет фото"

    get_html_photo.short_description = "Миниатюра"
