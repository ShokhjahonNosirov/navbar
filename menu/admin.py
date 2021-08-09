from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Genre
# Register your models here.
admin.site.register(Genre, MPTTModelAdmin)
