from django.contrib import admin
from .models import *

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ciudad", "telefono", "email")


@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ("matriz","direccion","ciudad","maps_link")


@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    search_fields = ("titulo", "contenido")

@admin.register(Caract_Servicios)
class Caract_ServiciosAdmin(admin.ModelAdmin):
    list_display = ("orden","titulo","detalle")


@admin.register(Info_web)
class InfoWebAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'publicado')
    list_filter = ('categoria', 'publicado')

@admin.register(Documentacion)
class DocumentacionAdmin(admin.ModelAdmin):
    list_display = ( 'categoria','titulo' )
