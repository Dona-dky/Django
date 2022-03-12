import django
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .models import Product
from .forms import ProductForm
from .forms import QuantityForm
from django.contrib.auth.decorators import login_required

# # Create your views here.
# def index(request):
#     return render(request,'beautyflowers/index.html')
@login_required
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
def read_product(request, slug):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed slug
    obj = get_object_or_404(Product, slug = slug)

    # add the dictionary during initialization
    form = QuantityForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + slug)
 
    # add the dictionary during initialization
    context["data"] = Product.objects.get(slug = slug)
         
    return render(request, "beautyflowers/crud/read_product.html", context)


# update product
def update_product(request, slug):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed slug
    obj = get_object_or_404(Product, slug = slug)
 
    # pass the object as instance in form
    form = ProductForm(request.POST or None, request.FILES or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "beautyflowers/crud/update_product.html", context)


# delete product
def delete_product(request, slug):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed slug
    obj = get_object_or_404(Product, slug = slug)
 
 
    if request.method =="POST":
        # delete the object post
        obj.delete()
        # after deleting redirect to
        # the list of post
        return HttpResponseRedirect("/")
 
    return render(request, "beautyflowers/crud/delete_product.html", context)


def cart_products(request):
    return render(request,'beautyflowers/cart.html')
