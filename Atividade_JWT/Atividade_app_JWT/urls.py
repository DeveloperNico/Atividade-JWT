from django.urls import path
from . import views

urlpatterns = [
    path('pessoas/', view=views.read_pessoas, name="read_pessoas"),
    path('pessoas/<int:pk>', view=views.read_pessoa, name="read_pessoa"),
    path('registrar/', view=views.registrar, name="registrar"),
    path('logar/', view=views.logar, name="logar"),
    path('atualizar/<int:pk>', view=views.update_pessoa, name="update_pessoa"),
    path('deletar/<int:pk>', view=views.delete_pessoa, name="delete_pessoa")
]