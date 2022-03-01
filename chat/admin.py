from django.contrib import admin
from chat.models import Room, Message

# Register your models here.

# Models will be accessible in Admin panel
admin.site.register(Room)
admin.site.register(Message)