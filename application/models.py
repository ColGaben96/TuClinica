from django.db import models


class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=255)


class TipoServicio(models.Model):
    nombre = models.CharField(max_length=255)
    tarifa = models.IntegerField


class TipoSuministro(models.Model):
    nombre = models.CharField(max_length=255)


class TipoIdentificacion(models.Model):
    nombre = models.CharField(max_length=255)


class Usuario(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.SET_NULL)
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.SET_NULL)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=255)
    estado = models.BooleanField()


class Pais(models.Model):
    nombre = models.CharField(max_length=255)


class Departamento(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL)


class Municipio(models.Model):
    nombre = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL)


class Direccion(models.Model):
    direccion = models.CharField(max_length=255)
    barrio = models.CharField(max_length=255)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL)


class Especie(models.Model):
    nombre = models.CharField(max_length=255)


class Raza(models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.ForeignKey(Especie, on_delete=models.SET_NULL)


class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    tamano = models.CharField(max_length=255)
    fecha_nacimiento = models.DateTimeField()
    detalles = models.CharField(max_length=255)
    dueno = models.ForeignKey(Usuario, on_delete=models.SET_NULL)
    estado = models.BooleanField()


class Factura(models.Model):
    dueno = models.ForeignKey(Usuario, on_delete=models.SET_NULL)
    veterinario = models.ForeignKey(Usuario, on_delete=models.SET_NULL)
    fecha_servicio = models.DateTimeField()
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.SET_NULL)
    total_servicio = models.IntegerField()
    estado = models.BooleanField()


class Historia(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL)
    servicio = models.ForeignKey(Factura, on_delete=models.SET_NULL)
    diagnostico = models.CharField(max_length=255)
    estado = models.BooleanField()


class Suministro(models.Model):
    nombre = models.CharField(max_length=255)
    via_administracion = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    precio = models.IntegerField()
    tipo_suministro = models.ForeignKey(TipoSuministro, on_delete=models.SET_NULL)


class HistoriaSuministro(models.Model):
    nombre = models.CharField(max_length=255)
    historia = models.ForeignKey(Historia, on_delete=models.SET_NULL)
    suministro = models.ForeignKey(Suministro, on_delete=models.SET_NULL)
