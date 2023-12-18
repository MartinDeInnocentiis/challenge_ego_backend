from django.contrib import admin
from extras.models import *


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'datetime', 'address']

@admin.register(Financing)
class FinancingAdmin(admin.ModelAdmin):
    list_display = ['id', 'jsonfield']