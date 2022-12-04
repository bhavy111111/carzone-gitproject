from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
'''
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src = "{}" width="40" style  = "border-radius:50px;" />'.format(object.car_photo.url))
    thumbnail.short_desccription = "Car Image"
    list_display = ('id' , 'car_title' , 'year','car_photo','color','transmission')
    search_fields = ('car_title' ,'id')
    list_display_links = ('car_title' , 'id' )

    #list_editable = ('is_featured',)
'''
admin.site.register(Car)
