from turtle import mode
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(blank=True)
    created_on = models.DateField(blank=True)

    # We add a Meta class to specify our model
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title