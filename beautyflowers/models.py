from email.policy import default
from django.db import models
import os

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=220)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(blank=True, default="Exclusive one-size poster.")
    image = models.ImageField(upload_to = "beautyflowers/static/img/", default=None)
    alt = models.CharField(max_length=50, null=False, default="img")
    quantity = models.IntegerField(default=0, blank=True, null=0)
    last_modified = models.DateTimeField(auto_now_add = True)
    created_on = models.DateField(blank=True, null=True)

    # We add a Meta class to specify our model
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name