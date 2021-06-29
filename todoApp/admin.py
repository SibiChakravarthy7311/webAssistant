from django.contrib import admin
from .models import *

# Register your models here.


class todoAdmin(admin.ModelAdmin):
    list_display = ['id', 'task']


admin.site.register(TodoModel, todoAdmin)
