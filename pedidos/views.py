from django.shortcuts import render
from django.shortcuts import render, redirect
from entidad.models import Pedido

def mostrar_pedidos(request):
    if request.session.get('estado_sesion'):
        pedidos = Pedido.objects.all()
        datos = {
            'pedidos': pedidos,
            'nombre_usuario': request.session.get('nombre_usuario').upper()
        }
        return render(request, "pedidos_listado.html", datos)
    else:
        datos = {
            'r2': 'Debe iniciar sesión para ingresar a la página.'
        }
        return render(request, "index.html")


def registrar_pedido(request):
    if request.session.get('estado_sesion'):
        if request.method == 'POST':
            Pedido.objects.create(
                nombre_cliente=request.POST['nombre_cliente'],
                telefono=request.POST['telefono'],
                contorno_cadera=request.POST['contorno_cadera'],
                altura_cadera=request.POST['altura_cadera'],
                contorno_cintura=request.POST['contorno_cintura'],
                largo_pierna=request.POST['largo_pierna'],
                largo_tiro=request.POST['largo_tiro'],
                largo_rodilla=request.POST['largo_rodilla'],
                ancho_pantalon=request.POST['ancho_pantalon'],
                fecha_entrega=request.POST['fecha_entrega'],
                valor_pedido=request.POST['valor_pedido'],
                estado_confeccion=request.POST['estado_confeccion'],
                estado_pago=request.POST['estado_pago'],
                tipo_corte=request.POST['tipo_corte'],
                observaciones=request.POST['observaciones']
            )
            return redirect('mostrar_pedidos')
        return render(request, "pedido_form.html")
    else:
        return render(request, "index.html")

# Create your views here.
