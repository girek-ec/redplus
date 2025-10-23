from django.db import models
from django.utils.text import slugify

class Segmento(models.TextChoices):
    HOGAR = "HOGAR", "Home"
    EMPRESA = "EMPRESA", "Empresa"

class Tecnologia(models.TextChoices):
    FIBRA = "FIBRA", "Fibra Óptica"
    WIRELESS = "WIRELESS", "Wireless"

class Plan(models.Model):
    activo = models.BooleanField(default=True, blank=True, null=True)
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    icono = models.CharField(max_length=40, blank=True, null=True)

    segmento = models.CharField(max_length=20, choices=Segmento.choices, default=Segmento.HOGAR)
    tecnologia = models.CharField(max_length=20, choices=Tecnologia.choices, default=Tecnologia.FIBRA)

    n_pantalla_gomax = models.IntegerField(default=0, blank=True, null=True)

    velocidad_mbps = models.PositiveIntegerField(help_text="Mbps")
    compresion = models.CharField(max_length=10, default="2:1", blank=True, null=True)
    simetrico = models.BooleanField(default=True, blank=True, null=True)

    precio_mensual = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=3, default="USD", blank=True, null=True)

    router = models.CharField(max_length=50, blank=True, null=True)
    beneficio = models.CharField(max_length=50, blank=True, null=True)

    destacado = models.BooleanField(default=False, blank=True, null=True)

    orden = models.PositiveIntegerField(default=0, blank=True, null=True)

    creado = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    actualizado = models.DateTimeField(auto_now=True, blank=True, null=True)


    class Meta:
        ordering = ("segmento", "tecnologia", "orden", "velocidad_mbps")
        verbose_name = "Plan"
        verbose_name_plural = "Planes"
        unique_together = (("segmento", "tecnologia", "velocidad_mbps", "nombre"),)

    def __str__(self):
        return f"{self.nombre} {self.velocidad_mbps}Mbps ({self.get_tecnologia_display()})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.nombre}-{self.velocidad_mbps}-{self.tecnologia}")
        super().save(*args, **kwargs)

    @property
    def precio_final(self):
        return self.precio_mensual
