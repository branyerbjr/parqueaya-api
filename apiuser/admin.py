<<<<<<< HEAD
from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'correo', 'fecha_registro')
    search_fields = ('nombres', 'apellidos', 'correo')
    readonly_fields = ('id', 'fecha_registro', 'usuario')

admin.site.register(Usuario, UsuarioAdmin)
=======
from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'correo', 'fecha_registro')
    search_fields = ('nombres', 'apellidos', 'correo')
    readonly_fields = ('id', 'fecha_registro', 'usuario')

admin.site.register(Usuario, UsuarioAdmin)
>>>>>>> c96de7ee265198347df3f9c5d11e523b4645620e
