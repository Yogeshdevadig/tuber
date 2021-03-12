from django.contrib import admin
from .models import Hiretuber

# Register your models here.

class HiretuberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'tuber_id','tuber_name')
    list_display_links = ('id',)
    search_fields = ('first_name', 'tuber_id', 'tuber_name',)


admin.site.register(Hiretuber,HiretuberAdmin)