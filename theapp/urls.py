from django.urls import path
from . import views

# importing views from views..py
from .views import delete_post

app_name ='theapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_post, name='create_post'),
    path('list', views.list_post, name='list_post'),
    path('<id>', views.post_detail ),
    path('<id>/update', views.update_post ),
    path('<id>/delete', delete_post ),
]
