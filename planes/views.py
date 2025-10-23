from django.shortcuts import render, get_object_or_404
from .models import Plan, Segmento, Tecnologia
from principal.models import Empresa, Pagina


def planes_home(request):
    qs = (Plan.objects
          .filter(activo=True, segmento=Segmento.HOGAR)
          .order_by("tecnologia", "orden", "velocidad_mbps"))
    contexto = {
        "planes_fibra": qs.filter(tecnologia=Tecnologia.FIBRA),
        "planes_wireless": qs.filter(tecnologia=Tecnologia.WIRELESS),
        "marca": Empresa.objects.first(),
        'pagina': Pagina.objects.all().first(),
    }
    return render(request, "planes/planes_home.html", contexto)

def planes_por_tecnologia(request, tecnologia_slug):
    map_slug = {"fibra": Tecnologia.FIBRA, "wireless": Tecnologia.WIRELESS}
    tecnologia = map_slug.get(tecnologia_slug)
    if tecnologia is None:
        return render(request, "planes/planes_por_tecnologia.html",
                      {"planes": [], "tecnologia_slug": tecnologia_slug, "marca": Empresa.objects.first()})
    planes = (Plan.objects
              .filter(activo=True, tecnologia=tecnologia, segmento=Segmento.HOGAR)
              .order_by("orden", "velocidad_mbps"))
    return render(request, "planes/planes_por_tecnologia.html",
                  {"planes": planes, "tecnologia_slug": tecnologia_slug, "marca": Empresa.objects.first()})

def plan_detalle(request, slug):
    plan = get_object_or_404(Plan, slug=slug, activo=True)
    return render(request, "planes/plan_detalle.html", {"plan": plan, "marca": Empresa.objects.first()})
