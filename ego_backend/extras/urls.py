from django.urls import path, include
from .views import *


urlpatterns = [

    path('activities/', ActivityListAPIView.as_view(), name='activity-list'),
    path('financing/', FinancingListAPIView.as_view(), name='financing-list'),


]