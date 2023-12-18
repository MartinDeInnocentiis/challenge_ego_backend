from django.urls import path
from .views import *


urlpatterns = [
    
    #Vehicle URLs
    path('vehicles/list/', ListVehicleAPIView.as_view(), name='list_vehicles'),
    path('vehicles/create/', PostVehicleAPIView.as_view(), name='create_vehicles'),
    path('vehicles/retrieve-update/<int:pk>/', RetrieveUpdateVehicleAPIView.as_view(), name='update_vehicles'),
    path('vehicles/delete/<int:pk>/', DestroyVehicleAPIView.as_view(), name='delete_vehicles'),
    path('vehicles/retrieve/<int:pk>/', GetOneVehicleAPIView.as_view(), name='get_one_vehicle'),
    
    #Dealership URLs
    path('dealerships/list/', ListDealershipAPIView.as_view(), name='list_dealerships'),
    path('dealerships/create/', CreateDealershipAPIView.as_view(), name='create_dealership'),
    path('dealerships/retrieve-update/<int:pk>/', RetrieveUpdateDealershipAPIView.as_view(), name='update_dealership'),
    path('dealerships/delete/<int:pk>/', DestroyDealershipAPIView.as_view(), name='delete_dealership'),
    path('dealerships/retrieve/<int:pk>/', RetrieveDealershipAPIView.as_view(), name='get_one_dealership'),
    
    #Category URLs
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    
    #VehicleDetail URLs
    path('vehicle-details/', VehicleDetailListCreateAPIView.as_view(), name='vehicle-detail-list'),
    path('vehicle-details/<int:pk>/', VehicleDetailRetrieveUpdateDestroyAPIView.as_view(), name='vehicle-detail-detail'),
    
    #Service URLs
    path('services/', ServiceListCreateAPIView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service-detail'),

    #Accessory URLs
    path('accessories/', AccessoryListCreateAPIView.as_view(), name='accessory-list'),
    path('accessories/<int:pk>/', AccessoryRetrieveUpdateDestroyAPIView.as_view(), name='accessory-detail'),

]
