from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Posts

@admin.register(Posts)
class PostUserAdmin(ModelAdmin):
    pass