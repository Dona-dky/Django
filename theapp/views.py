import django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Product
from django.utils import timezone

# Create your views here.
def index():
    return render('theapp/index.html')