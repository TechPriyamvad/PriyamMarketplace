from django.contrib import admin
from .models import Category,Item

# Register your models here so that model is visible in dashboard.
admin.site.register(Category)
admin.site.register(Item)