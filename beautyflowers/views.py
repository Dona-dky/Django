import django
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

#from .models import Product

# Create your views here.
def index(request):
    return render(request,'beautyflowers/index.html')