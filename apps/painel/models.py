from django.db import models
from django.utils import timezone


# Create your models here.

class Email(models.Model):
    choice={
        ('N','Não lido'),
        ('L','Lido')
    }
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    date = models.DateField(default=timezone.now)
    status = models.CharField(choices=choice, max_length=10, default='N')

    
    def __str__(self):
        return self.email