
from django.contrib import admin
from .models import Juego, Resena


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'plataforma',
        'anio_lanzamiento'
    )

    search_fields = ('titulo',)

    list_filter = ('plataforma', 'anio_lanzamiento')


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = (
        'juego',
        'usuario',
        'calificacion',
        'fecha_publicacion'
    )

    list_filter = ('calificacion',)
