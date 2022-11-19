from django.contrib import admin
from .models import Room, Message
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('slug',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'room', 'date_added', 'content')
    list_filter = ('user', 'room')
    ordering = ('-date_added',)

admin.site.register(Room, RoomAdmin)

admin.site.register(Message, MessageAdmin)
