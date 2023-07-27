from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Farmer, Field, Crop, Season

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Field)
class FieldAdmin(LeafletGeoAdmin):
    list_display = ( 'farmer', 'pole',)
    list_filter = ('farmer',)
    search_fields = ('name', 'farmer__name')
    settings_overrides = {
        'DEFAULT_CENTER': (51.5, -0.1),
        'DEFAULT_ZOOM': 12,
    }

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
