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



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

