from django.db import models

class Medida(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    unidad = models.CharField(max_length=10, blank=False, null=False)

class EstadoProducto(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)

class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=False)
    precio_unitario = models.PositiveIntegerField(blank=False, null=False)
    cantidad = models.PositiveIntegerField(default=1, blank=False, null=False)
    estado_producto = models.ForeignKey(EstadoProducto, on_delete=models.CASCADE, related_name='estados_productos')

class ProductoMedida(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='productos')
    medidas = models.ForeignKey(Medida, on_delete=models.CASCADE, related_name='medidas')
    longitud = models.PositiveIntegerField(blank=False, null=False)