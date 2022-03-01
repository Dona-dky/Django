from django.urls import path
from . import views

app_name ='beautyflowers'
urlpatterns = [
    path('', views.index, name='index'),
]
