from django.contrib import admin
from .models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("nombre", "segmento", "icono", "tecnologia", "velocidad_mbps",
                    "compresion", "simetrico", "precio_mensual", "destacado","router","beneficio", "activo", "orden")
    list_filter = ("segmento", "tecnologia", "simetrico", "destacado", "activo")
    list_editable = ("destacado", "activo", "orden", "precio_mensual")
    search_fields = ("nombre", "slug")
    prepopulated_fields = {"slug": ("nombre",)}
    ordering = ("segmento", "tecnologia", "orden", "velocidad_mbps")
