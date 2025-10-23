# apps/principal/views.py
from principal.models import *
from planes.models import *
from .forms import ContactForm  # tu form
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
        'planes': Plan.objects.all(),
        'sucursal': Sucursal.objects.all(),
        'documentaciones': Documentacion.objects.all(),
    }

    return render(request, 'index.html', contexto)


def iconos(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }

    return render(request, 'icons_catalog.html', contexto)

def info_cliente(request):
    contexto = {
        'marca': Empresa.objects.first(),
        'pagina': Pagina.objects.first(),
        'caract_serv': Caract_Servicios.objects.all(),
        'seguridad': Info_web.objects.filter(categoria='seguridad', publicado=True),
        'ancho_banda': Info_web.objects.filter(categoria='ancho_banda', publicado=True),
    }
    return render(request, 'informacion.html', contexto)



def contacto(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
        'sucursal': Sucursal.objects.all(),
    }

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            try:
                # Construye el correo en HTML con estilo más profesional
                html_content = f"""
                <div style="font-family: Arial, sans-serif; color: #333;">
                    <h2>Nuevo mensaje desde tu formulario de contacto web RedPlus</h2>
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr>
                            <td style="padding: 8px; font-weight: bold; vertical-align: top; width: 30%;">Nombre:</td>
                            <td style="padding: 8px; border-bottom: 1px solid #eee;">{nombre}</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px; font-weight: bold; vertical-align: top;">Email:</td>
                            <td style="padding: 8px; border-bottom: 1px solid #eee;">{email}</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px; font-weight: bold; vertical-align: top;">Asunto:</td>
                            <td style="padding: 8px; border-bottom: 1px solid #eee;">{asunto}</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px; font-weight: bold; vertical-align: top;">Mensaje:</td>
                            <td style="padding: 8px; border-bottom: 1px solid #eee;">{mensaje}</td>
                        </tr>
                    </table>
                    <p style="margin-top: 20px; font-size: 0.9em; color: #555;">
                        Este mensaje fue enviado desde el formulario de contacto de tu sitio web.
                    </p>
                </div>
                """

                email_message = EmailMessage(
                    subject=f"[RedPlus Web] {asunto}",
                    body=html_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.CONTACT_RECIPIENT]
                )
                email_message.content_subtype = "html"  # indica que es HTML
                email_message.send()

                messages.success(request, "Mensaje enviado correctamente.")
                return redirect('contacto')  # evita reenvío al refrescar
            except Exception as e:
                messages.error(request, f"Error enviando el mensaje: {e}")
    else:
        form = ContactForm()

    contexto['form'] = form
    return render(request, 'contacto.html', contexto)


def en_vivo(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }

    return render(request, 'servicios/servicio_transmision.html', contexto)


def hotspot(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'servicios/servicio_hotspot.html', contexto)

def go_max(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'go_max.html', contexto)

def calidad(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }

    return render(request, 'info_cliente/calidad.html', contexto)

def test_velocidad(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }

    return render(request, 'info_cliente/test_velocidad.html', contexto)

def consumo(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }

    return render(request, 'info_cliente/consumo.html', contexto)





def documentacion(request, id):
    # obtener el objeto específico y pasarlo como 'documentacion' (singular)
    doc = get_object_or_404(Documentacion, id=id)
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
        'documentacion': doc,
    }
    return render(request, 'documentacion.html', contexto)






def politica_privacidad(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
        'documentaciones': Documentacion.objects.all(),
    }
    return render(request, 'politicas/politica_privacidad.html', contexto)


def terminos_condiciones(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/terminos_condiciones.html', contexto)


def politica_cookies(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/politica_cookies.html', contexto)


def uso_servicio(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/uso_servicio.html', contexto)


def tratamiento_datos(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/tratamiento_datos.html', contexto)


def politica_seguridad(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/politica_seguridad.html', contexto)


def beneficios_adulto_mayor(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/beneficios_adulto_mayor.html', contexto)


def contrato_adhesion_clientes(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/contrato_adhesion_clientes.html', contexto)


def arcotel(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/arcotel.html', contexto)


def reclamos_arcotel(request):
    # puedes pasar el número en el contexto si quieres
    return render(request, 'politicas/reclamos_arcotel.html', {'telefono': '1800-567567'})


def normas_calidad_servicio(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/normas_calidad_servicio.html', contexto)


def ley_discapacidades(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/ley_discapacidades.html', contexto)


def ley_adulto_mayor(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/ley_adulto_mayor.html', contexto)


def reglamento_abonados(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/reglamento_abonados.html', contexto)


def guia_control_parental(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/guia_control_parental.html', contexto)


def uso_canal(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/uso_canal.html', contexto)


def info_basica(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/info_basica.html', contexto)


def beneficios_discapacidades(request):
    contexto = {
        'marca': Empresa.objects.all().first(),
        'pagina': Pagina.objects.all().first(),
        'caract_serv': Caract_Servicios.objects.all(),
    }
    return render(request, 'politicas/beneficios_discapacidades.html', contexto)
