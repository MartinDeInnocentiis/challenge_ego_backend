from django.db import models
from django.utils import timezone


class Activity(models.Model):
    name=models.CharField(max_length=30, blank=False, null=False)
    description=models.TextField(blank=True, null=True)
    datetime=models.DateTimeField(blank=True, null=True)
    address=models.CharField(max_length=70, blank=True, null=False)
    
    def __str__(self):
        return f'{self.name}'
    

class Financing(models.Model):
    jsonfield=models.JSONField(blank=False, null=False)
    
    def __str__(self):
        return f'{self.jsonfield}'
    
    