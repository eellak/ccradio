from ccradio.panel.models import Broadcaster, Category, Stream
from django.contrib import admin
from django.contrib.auth.models import User

class BroadcasterAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'stream', 'url')
    list_filter = ('category', 'stream')
    ordering = ('title', 'category')
    search_fields = ('title',)

admin.site.register(Broadcaster, BroadcasterAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)

class StreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'uri',)
    ordering = ('uri',)

admin.site.register(Stream, StreamAdmin)
