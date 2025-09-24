from django.contrib import admin
from entidad import models

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Usuario, UsuarioAdmin)

class PantalonAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Pantalon, PantalonAdmin)