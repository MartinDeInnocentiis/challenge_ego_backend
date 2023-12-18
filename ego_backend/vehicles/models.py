from django.db import models
from django.utils import timezone


class Dealership(models.Model):
    name=models.CharField(max_length=30, blank=False, null=False)
    address=models.CharField(max_length=70, blank=False, null=False)
    phone_number=models.CharField(max_length=30, blank=False, null=False)
    email=models.CharField(max_length=40, blank=False, null=False)
    
    def __str__(self):
        return f'{self.name}'
    

class Category(models.Model):
    name=models.CharField(max_length=70, blank=False, null=False)
    
    def __str__(self):
        return f'{self.name}'
    
    
class Vehicle(models.Model):
    category=models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    name=models.CharField(max_length=70, blank=False, null=False)
    year=models.PositiveIntegerField(blank=False, null=False)
    price=models.FloatField(max_length=11, default=0.00)
    img=models.URLField(blank=True, null=True)
    colors=models.JSONField(blank=False, null=False)
    version=models.JSONField(blank=False, null=False)
    created_at=models.DateTimeField(blank=False, null=False, default=timezone.now)
    updated_at=models.DateTimeField(blank=True, null=True)
    dealerships=models.ManyToManyField(Dealership)
    stock = models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return f'{self.name}'
    
    
class VehicleDetail(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    description = models.TextField()
    img = models.URLField(blank=True, null=True)
    specs = models.JSONField()

    def __str__(self):
        return f'{self.title}'
    
    
class Service(models.Model):
    name=models.CharField(max_length=70, blank=False, null=False)
    price=models.FloatField(max_length=11, default=0.00)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=80)
    dealerships=models.ManyToManyField(Dealership)
    for_clients=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
    
    
class Accessory(models.Model):
    name=models.CharField(max_length=70, blank=False, null=False)
    price=models.FloatField(max_length=11, default=0.00)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    dealerships=models.ManyToManyField(Dealership)

    def __str__(self):
        return f'{self.name}'
    