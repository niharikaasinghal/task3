from django.contrib import admin
from .models import person,blog

# Register your models here.
admin.site.register(person)
admin.site.register(blog)