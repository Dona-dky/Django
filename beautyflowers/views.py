import django
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .models import Product
from .forms import ProductForm


# Create your views here.
def index(request):
    return render(request,'beautyflowers/index.html')

def create_product(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list")
    
    context['form']= form
    return render(request, 'beautyflowers/crud/create_product.html', context)
