from django import forms
from .models import WeatherQuery

class WeatherQueryForm(forms.ModelForm):
    class Meta:
        model = WeatherQuery
        fields = ['city', 'temperature', 'description']