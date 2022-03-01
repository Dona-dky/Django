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


def list_of_products(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Product.objects.all()
         
    return render(request, "beautyflowers/index.html", context)


# after updating it will redirect to post_detail
def read_product(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)
         
    return render(request, "beautyflowers/crud/read_product.html", context)


