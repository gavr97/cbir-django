from django import forms
from django.forms import ModelForm

from .models import Database, Event

FILE_MAX_LENGTH = 100

file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class DatabaseForm(ModelForm):
    photos = forms.ImageField(required=False,
                              label='photos',
                              widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Database
        fields = ['date_added', 'title', 'slug', 'description', 'description_file']
        labels = {'description_file': 'Description file'}


class EventForm(ModelForm):
    query_photos = forms.ImageField(required=False,
                              label='query photos',
                              widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Event
        fields = ['date_added', 'title', 'slug', 'description', 'description_file']
        labels = {'description_file': 'Description file'}