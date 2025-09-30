# from django.shortcuts import render
# from entidad.models import Usuario, Pantalon
# #-------------------------------------------------------------------------------------

# def mostrar_index(request):
#     estado_sesion = request.session.get('estado_sesion')
#     if estado_sesion is True:
#         datos = {
#             'nombre_usuario': request.session.get('nombre_usuario').upper()
#         }
#         return render(request, "menu.html", datos)
#     else:
#         return render(request, "index.html")

# #-------------------------------------------------------------------------------------

# def mostrar_menu(request):
#     if request.method == 'POST':
#         usu = request.POST['txtusu']
#         con = request.POST['txtcon']
#         usuario_consulta = Usuario.objects.filter(nombre=usu, contrasena=con).values()
#         if usuario_consulta:
#             request.session['estado_sesion'] = True
#             request.session['id_usuario'] = usuario_consulta[0]['id']
#             request.session['nombre_usuario'] = usu.upper()

#             datos = {
#                 'nombre_usuario': usu.upper()
#             }

#             return render(request, "menu.html", datos)
#         else:
#             datos = {
#                 'r2': 'Usuario y/o contraseña incorrectos. Intente nuevamente.'
#             }
#             return render(request, "index.html", datos)
#     else:
#         datos = {
#             'r2': 'No se pudo procesar la solicitud.'
#         }
#         return render(request, "index.html", datos)
# #-------------------------------------------------------------------------------------

# def mostrar_listado(request):
#     estado_sesion = request.session.get('estado_sesion')
#     if estado_sesion is True:
#         pantalones = Pantalon.objects.all()
#         datos = {
#             'pantalones': pantalones,
#             'nombre_usuario': request.session.get('nombre_usuario').upper()
#         }
#         return render(request, "listado.html", datos)
#     else:
#         datos = {
#             'r2': 'Debe iniciar sesión para ingresar a la página.'
#         }
#         return render(request, "index.html", datos)

# #-------------------------------------------------------------------------------------

# def mostrar_form_reg(request):
#     try:
#         estado_sesion = request.session.get('estado_sesion')
#         if estado_sesion is True:
#             if request.method == 'POST':
#                 nombre_cliente = request.POST['nombre_cliente']
#                 telefono = request.POST['telefono']
#                 contorno_cadera = int(request.POST['contorno_cadera'])
#                 altura_cadera = int(request.POST['altura_cadera'])
#                 contorno_cintura = int(request.POST['contorno_cintura'])
#                 largo_pierna = int(request.POST['largo_pierna'])
#                 largo_tiro = int(request.POST['largo_tiro'])
#                 largo_rodilla = int(request.POST['largo_rodilla'])
#                 ancho_pantalon = int(request.POST['ancho_pantalon'])

#                 pantalon = Pantalon.objects.create(
#                     nombre_cliente = nombre_cliente,
#                     telefono = telefono,
#                     contorno_cadera = contorno_cadera,
#                     altura_cadera = altura_cadera,
#                     contorno_cintura = contorno_cintura,
#                     largo_pierna = largo_pierna,
#                     largo_tiro = largo_tiro,
#                     largo_rodilla = largo_rodilla,
#                     ancho_pantalon = ancho_pantalon
#                 )
#                 pantalon.save()
#                 datos = {
#                     'r1': 'Pantalón agregado exitosamente.',
#                     'nombre_usuario': request.session.get('nombre_usuario').upper(),
#                 }
#                 return render(request, "form_reg.html", datos)
#             else:
#                 datos = {
#                     'nombre_usuario': request.session.get('nombre_usuario').upper()
#                 }
#                 return render(request, "form_reg.html", datos)
#         else:
#             datos = {
#                 'r2': 'Debe iniciar sesión para ingresar a la página.',
#                 'nombre_usuario': request.session.get('nombre_usuario').upper()
#             }
#             return render(request, "index.html", datos)
#     except ValueError as e:
#         datos = {
#             'r2': f'Error al procesar el formulario. Ingrese datos válidos.',
#             'nombre_usuario': request.session.get('nombre_usuario').upper()
#         }
#         return render(request, 'form_reg.html', datos)
#     except Exception as e:
#         datos = {
#             'r2': f'Error inesperado: {e}',
#             'nombre_usuario': request.session.get('nombre_usuario').upper()
#         }
#         return render(request, 'form_reg.html', datos)


# #-------------------------------------------------------------------------------------

# def mostrar_form_act(request, pantalon_id):
#     try:
#         estado_sesion = request.session.get('estado_sesion')
#         if estado_sesion is True:
#             if request.method == 'POST':
#                 nombre_cliente = request.POST['nombre_cliente']
#                 telefono = request.POST['telefono']
#                 contorno_cadera = int(request.POST['contorno_cadera'])
#                 altura_cadera = int(request.POST['altura_cadera'])
#                 contorno_cintura = int(request.POST['contorno_cintura'])
#                 largo_pierna = int(request.POST['largo_pierna'])
#                 largo_tiro = int(request.POST['largo_tiro'])
#                 largo_rodilla = int(request.POST['largo_rodilla'])
#                 ancho_pantalon = int(request.POST['ancho_pantalon'])
                
#                 pantalon = Pantalon.objects.get(pk=pantalon_id)
#                 pantalon.nombre_cliente = nombre_cliente
#                 pantalon.telefono = telefono
#                 pantalon.contorno_cadera = contorno_cadera
#                 pantalon.altura_cadera = altura_cadera
#                 pantalon.contorno_cintura = contorno_cintura
#                 pantalon.largo_pierna = largo_pierna
#                 pantalon.largo_tiro = largo_tiro
#                 pantalon.largo_rodilla = largo_rodilla
#                 pantalon.ancho_pantalon = ancho_pantalon
                    
#                 pantalon.save()
#                 pantalones = Pantalon.objects.all()
#                 datos = {
#                     'pantalones': pantalones,
#                     'nombre_usuario': request.session.get('nombre_usuario').upper(),
#                     'r1': 'Registro modificado exitosamente.'
#                 }
#                 return render(request, "listado.html", datos)
#             else:
#                 pantalon = Pantalon.objects.get(pk=pantalon_id)

#                 datos = {
#                     'pantalon': pantalon,
#                     'nombre_usuario': request.session.get('nombre_usuario').upper()
#                 }
#                 return render(request, "form_act.html", datos)
#         else:
#             datos = {
#                 'r2': 'Debe iniciar sesión para ingresar a la página.'
#             }
#             return render(request, "index.html", datos)
#     except Pantalon.DoesNotExist as e:
#         pantalones = Pantalon.objects.all()
#         datos = {
#             'r2': f'El registro {pantalon_id} no existe. Intente nuevamente.',
#             'nombre_usuario': request.session.get('nombre_usuario').upper(),
#             'pantalones': pantalones
#         }
#         return render(request, 'listado.html', datos)
#     except ValueError as e:
#         pantalon = Pantalon.objects.get(pk=pantalon_id)
#         datos = {
#             'r2': f'Error al procesar el formulario. Ingrese datos válidos.',
#             'pantalon': pantalon
#         }
#         return render(request, 'form_act.html', datos)
#     except Exception as e:
#         pantalon = Pantalon.objects.get(pk=pantalon_id)
#         datos = {
#             'r2': f'Error inesperado: {e}',
#             'pantalon': pantalon
#         }
#         return render(request, 'form_act.html', datos)


# #-------------------------------------------------------------------------------------

# def eliminar_registro(request, pantalon_id):  
#     try:
#         estado_sesion = request.session.get('estado_sesion')
#         if estado_sesion is True:
#             pantalon = Pantalon.objects.get(pk=pantalon_id)
#             if pantalon:
#                 pantalon.delete()
#                 pantalones = Pantalon.objects.all()
#                 datos = {
#                     'r1': f'El registro {pantalon_id} fue eliminado exitosamente.',
#                     'nombre_usuario': request.session.get('nombre_usuario').upper(),
#                     'pantalones': pantalones
#                 }
#                 return render(request, 'listado.html', datos)
#             else:
#                 pantalones = Pantalon.objects.all()
#                 datos = {
#                     'r2': f'El registro {pantalon_id} no existe. Intente nuevamente.',
#                     'nombre_usuario': request.session.get('nombre_usuario').upper(),
#                     'pantalones': pantalones
#                 }
#                 return render(request, 'listado.html', datos)
#         else:
#             datos = {
#                 'r2': 'Debe iniciar sesión para realizar esta acción',
#             }
#             return render(request, 'index.html')
#     except Pantalon.DoesNotExist as e:
#         pantalones = Pantalon.objects.all()
#         datos = {
#             'r2': f'El registro {pantalon_id} no existe. Intente nuevamente.',
#             'nombre_usuario': request.session.get('nombre_usuario').upper(),
#                     'pantalones': pantalones
#         }
#         return render(request, 'listado.html', datos)
# #-------------------------------------------------------------------------------------

# def cerrar_sesion(request):
#     try:
#         del request.session["estado_sesion"]
#         del request.session["id_usuario"]
#         del request.session["nombre_usuario"]
        
#         return render(request,"index.html")
#     except:
#         return render(request,"index.html")

# #-------------------------------------------------------------------------------------
