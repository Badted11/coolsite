from django.db import models
from django.contrib.auth.models import User

class FavoriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city_name} (избранное {self.user.username})"

class WeatherHistory(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    date_checked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} — {self.temperature}°C, {self.description} ({self.date_checked})"

class WeatherQuery(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    date_checked = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='weather_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.city} — {self.temperature}°C"
