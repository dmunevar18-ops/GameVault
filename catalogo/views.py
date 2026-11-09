
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms

from .models import Juego, Resena


# FORMULARIO DE RESEÑAS

class ResenaForm(forms.ModelForm):

    class Meta:
        model = Resena
        fields = ['comentario', 'calificacion']

        widgets = {
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu opinión sobre el videojuego...',
                'rows': 4
            }),

            'calificacion': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


# INICIO Y CATÁLOGO

def inicio(request):

    juegos = Juego.objects.all().order_by('titulo')

    return render(
        request,
        'catalogo/inicio.html',
        {
            'juegos': juegos
        }
    )


# DETALLES DEL VIDEOJUEGO

def detalle_juego(request, id):

    juego = get_object_or_404(Juego, id=id)

    resenas = Resena.objects.filter(
        juego=juego
    ).select_related('usuario').order_by('-fecha_publicacion')

    return render(
        request,
        'catalogo/detalle.html',
        {
            'juego': juego,
            'resenas': resenas
        }
    )


# CREAR UNA RESEÑA

@login_required
def crear_resena(request, id):

    juego = get_object_or_404(Juego, id=id)

    if request.method == 'POST':

        formulario = ResenaForm(request.POST)

        if formulario.is_valid():

            resena = formulario.save(commit=False)
            resena.juego = juego
            resena.usuario = request.user
            resena.save()

            messages.success(
                request,
                'Tu reseña se publicó correctamente.'
            )

            return redirect(
                'detalle_juego',
                id=juego.id
            )

    else:

        formulario = ResenaForm()

    return render(
        request,
        'catalogo/formulario.html',
        {
            'formulario': formulario,
            'juego': juego
        }
    )


# EDITAR UNA RESEÑA PROPIA

@login_required
def editar_resena(request, id):

    resena = get_object_or_404(
        Resena,
        id=id,
        usuario=request.user
    )

    if request.method == 'POST':

        formulario = ResenaForm(
            request.POST,
            instance=resena
        )

        if formulario.is_valid():

            formulario.save()

            messages.success(
                request,
                'Tu reseña fue actualizada correctamente.'
            )

            return redirect(
                'detalle_juego',
                id=resena.juego.id
            )

    else:

        formulario = ResenaForm(instance=resena)

    return render(
        request,
        'catalogo/formulario.html',
        {
            'formulario': formulario,
            'resena': resena,
            'juego': resena.juego
        }
    )


# ELIMINAR UNA RESEÑA PROPIA

@login_required
def eliminar_resena(request, id):

    resena = get_object_or_404(
        Resena,
        id=id,
        usuario=request.user
    )

    if request.method == 'POST':

        juego_id = resena.juego.id

        resena.delete()

        messages.success(
            request,
            'Tu reseña fue eliminada correctamente.'
        )

        return redirect(
            'detalle_juego',
            id=juego_id
        )

    return render(
        request,
        'catalogo/eliminar.html',
        {
            'resena': resena
        }
    )


# REGISTRO DE USUARIOS

def registro(request):

    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':

        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():

            usuario = formulario.save()

            login(request, usuario)

            messages.success(
                request,
                'Tu cuenta fue creada correctamente.'
            )

            return redirect('inicio')

    else:

        formulario = UserCreationForm()

    return render(
        request,
        'catalogo/registro.html',
        {
            'formulario': formulario
        }
    )
