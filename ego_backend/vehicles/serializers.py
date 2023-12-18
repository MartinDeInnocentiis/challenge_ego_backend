from rest_framework import serializers
from .models import Vehicle, Dealership, Category, VehicleDetail, Service, Accessory


class DealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dealership
        fields=['id','name','address','phone_number','email']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']
        
class VehicleSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        write_only=True
    )
    dealerships = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Dealership.objects.all(), 
        write_only=True
    )
    dealership_names = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model=Vehicle
        fields=['id', 'category', 'category_name', 'name', 'year', 'price', 'version', 'img', 'colors', 'created_at','updated_at','dealerships', 'dealership_names', 'stock']
        
    def get_category_name(self, obj):
        return obj.category.name if obj.category else None
    
    def get_dealership_names(self, obj):
        return [dealership.name for dealership in obj.dealerships.all()]
    
    
class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetail
        fields = ['id', 'vehicle', 'title', 'description', 'img', 'specs']
        
        
class ServiceSerializer(serializers.ModelSerializer):
    dealerships = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Dealership.objects.all(), 
        write_only=True
    )
    dealership_names = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Service
        fields = ['id','name', 'price', 'description', 'duration', 'dealerships', 'for_clients', 'dealership_names']
        
    def get_dealership_names(self, obj):
        return [dealership.name for dealership in obj.dealerships.all()]

class AccessorySerializer(serializers.ModelSerializer):
    dealerships = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Dealership.objects.all(), 
        write_only=True
    )
    dealership_names = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Accessory
        fields = ['id', 'name', 'price', 'description', 'stock', 'dealerships', 'dealership_names']
        
    def get_dealership_names(self, obj):
        return [dealership.name for dealership in obj.dealerships.all()]