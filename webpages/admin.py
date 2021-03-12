from django.contrib import admin
from .models import*
from django.utils.html import format_html

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="50" style="border-radius:50%"/>'.format(object.photo.url))
    list_display = ('id','myphoto','first_name','last_name','role','created_date')
    list_display_links = ('first_name',)
    search_fields = ('role',)
    list_filter = ('role',)

class SliderAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="50"  height="40"/>'.format(object.photo.url))

    list_display = ('id','myphoto', 'headline', 'button_text')
    list_display_links = ('headline','myphoto')
    search_fields = ('headline',)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'subject')
    list_display_links = ('fullname', 'email')
    search_fields = ('fullname',)


admin.site.register(Slider,SliderAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(ContactUsForm,ContactFormAdmin)
admin.site.register(Socialmedia)