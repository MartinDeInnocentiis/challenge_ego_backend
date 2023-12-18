from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    rating = models.FloatField(
        default=0.00, 
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )
    username = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.rating}'