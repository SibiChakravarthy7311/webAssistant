from django.contrib import admin
from .models import *

# Register your models here.


class pageElementAdmin(admin.ModelAdmin):
    list_display = ['id', 'elementName']


class outlierElementAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


admin.site.register(pageElementModel, pageElementAdmin)
admin.site.register(outlierElementModel, outlierElementAdmin)
