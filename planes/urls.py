from django.urls import path
from . import views

app_name = "planes"

urlpatterns = [
    path("", views.planes_home, name="home"),                             # /planes/
    path("t/<slug:tecnologia_slug>/", views.planes_por_tecnologia, name="por_tecnologia"),  # /planes/t/fibra
    path("<slug:slug>/", views.plan_detalle, name="detalle"),             # /planes/plan-x
]
