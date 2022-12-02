from django.contrib import admin
from .models import Team
# Register your models here.
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src = "{}" width="40" />'.format(object.photo.url))

    list_display = ('id','thumbnail','first_name','designation','create_date')
    list_display_links = ('first_name' , 'id')
    search_fields = ('first_name','last_name','designation')
admin.site.register(Team,TeamAdmin)
