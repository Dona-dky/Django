import django
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .models import Product
from .forms import ProductForm


# # Create your views here.
# def index(request):
#     return render(request,'beautyflowers/index.html')

def create_product(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context['form']= form
    return render(request, 'beautyflowers/crud/create_product.html', context)


def list_of_products(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Product.objects.all()
         
    return render(request, "beautyflowers/shop.html", context)


# after updating it will redirect to post_detail
def read_product(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)
         
    return render(request, "beautyflowers/crud/read_product.html", context)


# update product
def update_product(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = ProductForm(request.POST or None, request.FILES or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" +id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "beautyflowers/crud/update_product.html", context)


# delete product
def delete_product(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
 
    if request.method =="POST":
        # delete the object post
        obj.delete()
        # after deleting redirect to
        # the list of post
        return HttpResponseRedirect("/")
 
    return render(request, "beautyflowers/crud/delete_product.html", context)
    
