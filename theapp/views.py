import django
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request,'theapp/index.html')

def create_post(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form']= form
    return render(request, 'theapp/create_post.html', context)

def list_post(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Post.objects.all()
         
    return render(request, "theapp/list_post.html", context)


# after updating it will redirect to post_detail
def post_detail(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Post.objects.get(id = id)
         
    return render(request, "theapp/post_detail.html", context)


# update post for details
def update_post(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Post, id = id)
 
    # pass the object as instance in form
    form = PostForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/theapp/" +id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "theapp/update_post.html", context)