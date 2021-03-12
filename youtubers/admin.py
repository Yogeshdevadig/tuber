from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.


class YouAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="50"  />'.format(object.photo.url))


    list_display = ('id', 'myphoto', 'name', 'subs_count', 'is_featured')
    list_display_links = ('name',)
    search_fields = ('name', 'category', 'camera_type',)
    list_filter = ('city', 'category')
    list_editable = ('is_featured',)



admin.site.register(Youtuber,YouAdmin)