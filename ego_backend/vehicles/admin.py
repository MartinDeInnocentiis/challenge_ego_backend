from django.contrib import admin
from vehicles.models import *


@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone_number', 'email']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'year', 'price', 'created_at']


@admin.register(VehicleDetail)
class VehicleDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'vehicle', 'title', 'description']
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description', 'duration']
    
@admin.register(Accessory)
class AccessAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description', 'stock']