from django.contrib import admin

# Register your models here.
# en tu_app/admin.py

from django.contrib import admin
from .models import Proveedor, Path

admin.site.register(Proveedor)
admin.site.register(Path)
