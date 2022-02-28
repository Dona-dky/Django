from django.urls import path
from . import views

app_name ='theapp'
urlpatterns = [
    path('', views.index, name='index'),
]
