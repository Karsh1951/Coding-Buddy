from django.contrib import admin

# Register your models here.
#it allows room to be viewed and used in the admin panel
from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)