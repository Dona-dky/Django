import django
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Post
from .forms import PostForm

# Create your views here.
def index():
    return render('theapp/index.html')

def new_post(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form']= form
    return render(request, 'theapp/new_post.html', context)
