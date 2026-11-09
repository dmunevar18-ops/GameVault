
from django import forms
from .models import Resena


class ResenaForm(forms.ModelForm):

    class Meta:
        model = Resena

        fields = [
            'comentario',
            'calificacion'
        ]

        widgets = {
            'comentario': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe tu opinión sobre este videojuego...',
                    'rows': 4
                }
            ),

            'calificacion': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }

        labels = {
            'comentario': 'Tu reseña',
            'calificacion': 'Calificación (1 a 5 estrellas)'
        }
