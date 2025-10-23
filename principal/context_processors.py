# apps/principal/context_processors.py
from .models import Empresa

def empresa(request):
    # devuelve la primera empresa o None
    obj = Empresa.objects.order_by('id').first()
    return {"marca": obj}
