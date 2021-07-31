from django.contrib import admin
from .models import Category,groceryItems
# Register your models here.

admin.site.register(groceryItems)
admin.site.register(Category)