
from django.db import models
from django.contrib.auth.models import User


class Juego(models.Model):

    PLATAFORMAS = [
        ('PC', 'PC'),
        ('PlayStation', 'PlayStation'),
        ('Nintendo', 'Nintendo'),
        ('Xbox', 'Xbox'),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()

    plataforma = models.CharField(
        max_length=30,
        choices=PLATAFORMAS
    )

    anio_lanzamiento = models.PositiveIntegerField()

    # Imagen de portada del videojuego
    imagen = models.ImageField(
        upload_to='juegos/',
        blank=True,
        null=True,
        max_length=255
    )

    def __str__(self):
        return self.titulo


class Resena(models.Model):

    juego = models.ForeignKey(
        Juego,
        on_delete=models.CASCADE,
        related_name='resenas'
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    comentario = models.TextField()

    calificacion = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        default=5
    )

    fecha_publicacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.usuario.username} - {self.juego.titulo}"
