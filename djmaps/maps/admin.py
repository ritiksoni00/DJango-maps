from django.contrib import admin

# Register your models here.

from .models import PlaceInfo, Image


@admin.register(PlaceInfo)
class PlaceInfoAdmin(admin.ModelAdmin):
    list_display = ['info_about_place','place_name']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'img']