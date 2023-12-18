from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import response
from .models import Vehicle, Dealership, Category, VehicleDetail, Accessory, Service
from .serializers import *

# Vehicle Views
class ListVehicleAPIView(ListAPIView):
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer
    
    
class PostVehicleAPIView(CreateAPIView):
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer
    
    
class RetrieveUpdateVehicleAPIView(RetrieveUpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class DestroyVehicleAPIView(DestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
    
class GetOneVehicleAPIView(RetrieveAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    def get_queryset(self):
        
        vehicle_id = self.kwargs['pk']
        queryset = self.queryset.filter(id=vehicle_id)
        return queryset


# Dealership Views
class ListDealershipAPIView(ListAPIView):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer
    
    
class CreateDealershipAPIView(CreateAPIView):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer
    

class RetrieveUpdateDealershipAPIView(RetrieveUpdateAPIView):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer


class DestroyDealershipAPIView(DestroyAPIView):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer


class RetrieveDealershipAPIView(RetrieveAPIView):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        vehicles = Vehicle.objects.filter(dealerships=instance)  # Obtener vehículos relacionados
        vehicle_serializer = VehicleSerializer(vehicles, many=True)
        return response({
            'dealership': serializer.data,
            'vehicles': vehicle_serializer.data
        })
        
        
# Category Views
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
# VehicleDetail Views
class VehicleDetailListCreateAPIView(ListCreateAPIView):
    queryset = VehicleDetail.objects.all()
    serializer_class = VehicleDetailSerializer

class VehicleDetailRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = VehicleDetail.objects.all()
    serializer_class = VehicleDetailSerializer
    

# Service Views
class ServiceListCreateAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Accessory Views
class AccessoryListCreateAPIView(ListCreateAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer

class AccessoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer