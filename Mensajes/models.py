from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

class Mensaje(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['creacion']

class HiloAdministrador(models.Manager):
    def buscar(self, user1, user2):
        consulta = self.filter(usuarios=user1).filter(usuarios=user2)
        if len(consulta) > 0:
            return consulta[0]
        return None

    def buscar_o_crear(self, user1, user2):
        hilo = self.buscar(user1, user2)
        if hilo is None:
            hilo = Hilo.objects.create()
            hilo.usuarios.add(user1, user2)
        return hilo
        

class Hilo(models.Model):
    usuarios = models.ManyToManyField(User, related_name='hilos')
    mensajes = models.ManyToManyField(Mensaje)
    actualizacion = models.DateTimeField(auto_now=True)

    objects = HiloAdministrador()

    class Meta:
        ordering = ['-actualizacion']


def mensajes_cambiados(sender, **kwargs):
    instancia = kwargs.pop("instancia", None)
    accion = kwargs.pop("accion", None)
    pk_set = kwargs.pop("pk_set", None)
    print(instancia, accion, pk_set)

    false_pk_set = set()
    if accion is "pre_add":
        for msg_pk in pk_set:
            msg = Mensaje.objects.get(pk=msg_pk)
            if msg.user not in instancia.usuarios.all():
                print("Ups, ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk)

        instancia.save()

    pk_set.difference_update(false_pk_set)

m2m_changed.connect(mensajes_cambiados, sender=Hilo.mensajes.through)