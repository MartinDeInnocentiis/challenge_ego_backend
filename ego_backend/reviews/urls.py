from django.urls import path
from .views import *


urlpatterns = [

    path('reviews-list/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews-edit/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),

]