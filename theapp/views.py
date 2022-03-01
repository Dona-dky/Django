import django
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
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