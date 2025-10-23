# apps/principal/apps.py
from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "principal"

    def ready(self):
        # Importa aquí señales u otras integraciones que requieran los modelos.
        # Ejemplo (si las tienes):
        # from . import signals  # noqa: F401
        pass
