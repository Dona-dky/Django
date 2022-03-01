from django.contrib import admin

from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
  fields = ['text','date']

admin.site.register(Post)