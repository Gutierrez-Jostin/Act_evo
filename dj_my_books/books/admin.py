from django.contrib import admin

# Register your models here.
from .models import Category, Books

admin.site.register(Books)
admin.site.register(Category)

