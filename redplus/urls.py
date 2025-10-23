"""
URL configuration for redplus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# redplus/urls.py
from django.contrib import admin as django_admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from principal.views import *
import planes.admin

urlpatterns = [
    path("admin/", django_admin.site.urls),
    path("", index, name="home"),
    path("iconos/", iconos, name="icons_catalog"),
    path("planes/", include(("planes.urls", "planes"), namespace="planes")),
    path("__reload__/", include(("django_browser_reload.urls", "django_browser_reload"),
                                namespace="django_browser_reload")),  # ← clave

    path('informacion/',info_cliente,name="informacion"),
    path('hotspot/', hotspot, name='hotspot'),
    path('go_max/', go_max, name='go_max'),
    path('en_vivo/', en_vivo, name='en_vivo'),
    path('contacto/', contacto, name='politica_privacidad'),
    path('calidad/', calidad, name='calidad'),
    path('consumo/', consumo, name='consumo'),
    path('test_velocidad/', test_velocidad, name='test_velocidad'),
    path('contacto/', contacto, name='contacto'),

    path('documentaciones/<int:id>/', documentacion, name='documentacion'),


    path('politicas/politica_privacidad/', politica_privacidad, name='politica_privacidad'),
    path('politicas/terminos_condiciones/', terminos_condiciones, name='terminos_condiciones'),
    path('politicas/politica_cookies/', politica_cookies, name='politica_cookies'),
    path('politicas/uso_servicio/', uso_servicio, name='uso_servicio'),
    path('politicas/tratamiento_datos/', tratamiento_datos, name='tratamiento_datos'),
    path('politicas/politica_seguridad/', politica_seguridad, name='politica_seguridad'),
    path('politicas/beneficios_adulto_mayor/', beneficios_adulto_mayor, name='beneficios_adulto_mayor'),
    path('politicas/contrato_adhesion_clientes/', contrato_adhesion_clientes, name='contrato_adhesion_clientes'),
    path('politicas/arcotel/', arcotel, name='arcotel'),
    path('politicas/reclamos_arcotel/', reclamos_arcotel, name='reclamos_arcotel'),  # muestra 1800-567567
    path('politicas/normas_calidad_servicio/', normas_calidad_servicio, name='normas_calidad_servicio'),
    path('politicas/ley_discapacidades/', ley_discapacidades, name='ley_discapacidades'),
    path('politicas/ley_adulto_mayor/', ley_adulto_mayor, name='ley_adulto_mayor'),
    path('politicas/reglamento_abonados/', reglamento_abonados, name='reglamento_abonados'),
    path('politicas/guia_control_parental/', guia_control_parental, name='guia_control_parental'),
    path('politicas/uso_canal/', uso_canal, name='uso_canal'),
    path('politicas/info_basica/', info_basica, name='info_basica'),
    path('politicas/beneficios_discapacidades/', beneficios_discapacidades, name='beneficios_discapacidades'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

