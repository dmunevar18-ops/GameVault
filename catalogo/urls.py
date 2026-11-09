
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [

    path(
        '',
        views.inicio,
        name='inicio'
    ),

    path(
        'juego/<int:id>/',
        views.detalle_juego,
        name='detalle_juego'
    ),

    path(
        'juego/<int:id>/resena/',
        views.crear_resena,
        name='crear_resena'
    ),

    path(
        'resena/<int:id>/editar/',
        views.editar_resena,
        name='editar_resena'
    ),

    path(
        'resena/<int:id>/eliminar/',
        views.eliminar_resena,
        name='eliminar_resena'
    ),

    path(
        'registro/',
        views.registro,
        name='registro'
    ),

    path(
        'login/',
        LoginView.as_view(
            template_name='catalogo/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

]
