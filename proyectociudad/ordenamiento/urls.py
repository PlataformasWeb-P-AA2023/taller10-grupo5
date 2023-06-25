from django.urls import path
from . import views


urlpatterns = [
    # Parroquias
    path('', views.index, name='index'),
    path('crear/parroquia', views.crear_parroquia, name='crear_parroquia'),
    path('editar/parroquia/<int:id>', views.editar_parroquia, name='editar_parroquia'),
    path('eliminar/parroquia/<int:id>', views.eliminar_parroquia, name='eliminar_parroquia'),

    # Barrios
    path('barrios', views.listar_barrios, name='listar_barrios'),
    path('crear/barrio', views.crear_barrio, name='crear_barrio'),
    path('editar/barrio/<int:id>', views.editar_barrio, name='editar_barrio'),
    path('eliminar/barrio/<int:id>', views.eliminar_barrio, name='eliminar_barrio'),
    path('crear/barrio/parroquia/<int:id>', views.crear_barrio_parroquia, name='crear_barrio_parroquia'),
 ]
