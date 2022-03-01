from django.urls import path
from . import views

app_name ='theapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_post, name='create_post'),
    path('list', views.list_post, name='list_post'),
]
