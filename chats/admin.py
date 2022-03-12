from django.contrib import admin
from .models import Chat, ChatMessage

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
  fields = ['room_name']
admin.site.register(Chat)
admin.site.register(ChatMessage)