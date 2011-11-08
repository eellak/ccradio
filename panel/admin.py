from ccradio.panel.models import Broadcaster, Category
from django.contrib import admin
from django.contrib.auth.models import User

class BroadcasterAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'active', 'stream')
    list_filter = ('category', 'stream', 'active')
    ordering = ('title', 'category')
    search_fields = ('title',)

admin.site.register(Broadcaster, BroadcasterAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)

