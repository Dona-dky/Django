from turtle import mode
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    text = models.CharField(max_length=220)
    date = models.DateTimeField('date')
    def __str__(self):
        return self.text
    def publier(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)