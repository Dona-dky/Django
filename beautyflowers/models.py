from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=220)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = "beautyflowers/static/img/", null=True, blank=True)
    alt = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField()
    last_modified = models.DateTimeField(auto_now_add = True)
    created_on = models.DateField(blank=True, null=True)

    # We add a Meta class to specify our model
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name