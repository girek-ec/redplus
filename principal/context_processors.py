# apps/principal/context_processors.py
from .models import Empresa, Documentacion

def empresa(request):
    # devuelve la primera empresa o None
    obj = Empresa.objects.order_by('id').first()
    # devolver documentaciones para uso global en templates (ej. footer)
    documentaciones = Documentacion.objects.all()
    return {"marca": obj, "documentaciones": documentaciones}
