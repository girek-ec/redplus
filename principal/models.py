from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField


class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    lema = models.CharField(max_length=255, blank=True, help_text="Frase corta o slogan")
    detalle= models.TextField(  blank=True, null=True ,help_text="resumen de lo que es la empresa RedPlus")
    favicon = models.ImageField(upload_to="empresa/", blank=True, null=True)
    logo = models.ImageField(upload_to="empresa/", blank=True, null=True)
    logo_blanco = models.ImageField(upload_to="empresa/", blank=True, null=True)

    direccion = models.CharField(max_length=255, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    maps_link = models.URLField("Link Google Maps (Ruta)", blank=True)  # aquí pegas el shortlink o url de google maps
    maps_view = models.TextField(  blank=True, null=True) # aquí pegas el Incorporar un mapa de google maps el iframe

    test_velocidad = models.TextField(blank=True, null=True, help_text="Copiar aqui el iframe  codigo de test de velocidad")

    telefono = models.CharField(max_length=50, blank=True)
    whatsapp = models.CharField(max_length=50, blank=True, help_text="Número WhatsApp con código país")
    whatsapp_ventas = models.CharField(max_length=50, blank=True, help_text="Número WhatsApp con código país")
    whatsapp_info = models.CharField(max_length=50, blank=True, help_text="Número WhatsApp con código país")
    email = models.EmailField(blank=True)
    horario = models.CharField(max_length=200, blank=True, help_text="Ej. Lun-Vie 8:00-18:00")

    facebook = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50,blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    youtube = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresa"

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    matriz =models.BooleanField(default=False)
    ciudad = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    maps_link = models.URLField("Link Google Maps (Ruta)", blank=True ,help_text="aquí pegas el shortlink o url de google maps")
    maps_view = models.TextField(  blank=True, null=True ,help_text="aquí pegas el Incorporar un mapa de google maps sin el iframe src=")

    telefono = models.CharField(max_length=50, blank=True)
    whatsapp = models.CharField(max_length=50, blank=True, help_text="Número WhatsApp con código país")
    whatsapp_ventas = models.CharField(max_length=50, blank=True, help_text="Número WhatsApp con código país")
    whatsapp_info = models.CharField(max_length=50, blank=True, help_text="Número WhatsApp con código país")
    email = models.EmailField(blank=True)
    horario = models.CharField(max_length=200, blank=True, help_text="Ej. Lun-Vie 8:00-18:00")


    class Meta:
        verbose_name = "Sucursales"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.ciudad




class Pagina(models.Model):
    """Para secciones como 'Sobre nosotros', 'Misión', 'Visión', etc."""
    titulo = models.CharField(max_length=200, default="RedPlus", blank=True, null=True)
    img_1 = models.ImageField(upload_to="paginas/", blank=True, null=True,help_text="Imagen 1 para inciio slider")
    img_2 = models.ImageField(upload_to="paginas/", blank=True, null=True,help_text="Imagen 2 para inciio slider")
    img_3 = models.ImageField(upload_to="paginas/", blank=True, null=True,help_text="Imagen 3 para inciio slider")

    img_4 = models.ImageField(upload_to="paginas/", blank=True, null=True, help_text="Imagen  para  Conéctate con nosotros")
    img_5 = models.ImageField(upload_to="paginas/", blank=True, null=True, help_text="Imagen  para ")
    img_6 = models.ImageField(upload_to="paginas/", blank=True, null=True, help_text="Imagen  para")
    img_7 = models.ImageField(upload_to="paginas/", blank=True, null=True, help_text="Imagen  ")

    botarga_1 = models.ImageField(upload_to="paginas/", blank=True, null=True,help_text="mascota empresa")
    botarga_2 = models.ImageField(upload_to="paginas/", blank=True, null=True, help_text="mascota empresa")
    botarga_3 = models.ImageField(upload_to="paginas/", blank=True, null=True, help_text="mascota empresa")

    img_gomax_1 = models.ImageField(upload_to="paginas/", blank=True, null=True)
    img_gomax_2 = models.ImageField(upload_to="paginas/", blank=True, null=True)
    img_gomax_3 = models.ImageField(upload_to="paginas/", blank=True, null=True)
    img_serv_hotspot = models.ImageField(upload_to="paginas/", blank=True, null=True)
    img_serv_vivo = models.ImageField(upload_to="paginas/", blank=True, null=True)
    img_contacto = models.ImageField(upload_to="paginas/", blank=True, null=True)
    img_informacion= models.ImageField(upload_to="paginas/", blank=True, null=True,  help_text="Imagen horizontal sobre informacion al cliente")

    archivo_calidad = models.FileField(upload_to="paginas/", blank=True, null=True, help_text="Subir archivo pdf dispuestos por la ARCOTEL")
    img_calidad = models.ImageField(upload_to="paginas/", blank=True, null=True,  help_text="Imagen resolucion dispuestos por la ARCOTEL")
    img_consumo = models.ImageField(upload_to="paginas/", blank=True, null=True)
    class Meta:
        verbose_name = "Página Inicio"
        verbose_name_plural = "Página Inicio"

    def __str__(self):
        # Devuelve siempre una cadena. Prioriza título, luego pk, luego nombre de clase.
        if self.titulo:
            return str(self.titulo)
        if getattr(self, 'pk', None):
            return f"Página #{self.pk}"
        return "Página sin título"



class Caract_Servicios(models.Model):
    orden =models.IntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=100)
    icono = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to="caracteres/", blank=True, null=True)
    detalle = models.TextField(max_length=500, blank=True, null=True)


    class Meta:
        verbose_name = "Caracteristica de Servicios"
        verbose_name_plural = "Caracteristica de Servicios"

    def __str__(self):
        return self.titulo


class Info_web(models.Model):
    CATEGORY_CHOICES = [
        ('seguridad', 'Seguridad informática'),
        ('ancho_banda', 'Ancho de banda'),
    ]

    categoria = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    titulo = models.CharField(max_length=200)
    sub_titulo = models.CharField(max_length=250, blank=True)
    cuerpo = RichTextField(help_text="Editor avanzado para el contenido")
    publicado = models.BooleanField(default=True)
    orden = models.PositiveSmallIntegerField(default=0, help_text="Orden de aparición (menor = primero)")

    class Meta:
        verbose_name = "Información Web"
        verbose_name_plural = "Información Web"

    def __str__(self):
        return f"{self.titulo} ({self.get_categoria_display()})"


class Documentacion(models.Model):
    CATEGORY_CHOICES = [
        ('politica_regulaciones', 'Políticas y regulaciones'),
        ('legislacion_ayuda', 'Legislación y ayuda'),
        ('normas_beneficio', 'Normas y beneficios'),
        ('ayuda_rapida', 'Ayuda Rápida'),
    ]

    categoria = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    titulo = models.CharField(max_length=200)
    sub_titulo = models.CharField(max_length=250, blank=True)
    cuerpo = RichTextField(help_text="Editor avanzado para el contenido", blank=True, null=True)
    activar_link = models.BooleanField(default=False)
    link= models.CharField(max_length=250, blank=True , null=True, help_text="Link de información")
    archivo_pdf = models.FileField(upload_to="paginas/", blank=True, null=True, help_text="Subir archivo en pdf")
    orden = models.PositiveSmallIntegerField(default=0, help_text="Orden de aparición (menor = primero)")

    class Meta:
        verbose_name = "Documentacion"
        verbose_name_plural = "Documentacion"

    def __str__(self):
        return f"{self.titulo} ({self.get_categoria_display()})"