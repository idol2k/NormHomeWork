from django.contrib import admin
from .models import Posts
@admin.register(Posts)
class ViewAdmin(admin.ModelAdmin):
    pass
