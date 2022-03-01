from django.urls import path
from . import views

app_name ='beautyflowers'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_product, name='create_product'),
    # path('list', views.list_post, name='list_post'),
    # path('<id>', views.post_detail ),
    # path('<id>/update', views.update_post ),
    # path('<id>/delete', delete_post ),

]
