from django.urls import path
from . import views

app_name ='beautyflowers'
urlpatterns = [
    path('create', views.create_product, name='create_product'),
    path('', views.list_of_products, name='list_of_products'),
    path('<slug>', views.read_product ),
    path('<slug>/update', views.update_product ),
    path('<slug>/delete', views.delete_product ),
]
