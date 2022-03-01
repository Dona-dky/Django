from django.urls import path
from . import views

app_name ='beautyflowers'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_product, name='create_product'),
    path('list', views.list_of_products, name='list_of_products'),
    path('<id>', views.read_product ),
    path('<id>/update', views.update_product ),
    # path('<id>/delete', delete_post ),

]
