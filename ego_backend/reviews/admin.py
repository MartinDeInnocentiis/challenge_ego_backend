from django.contrib import admin
from reviews.models import *


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'username', 'content', 'created_at']

