from django.contrib import admin
from .models import Pessoa
from django.contrib.auth.admin import UserAdmin

class PessoaAdmin(UserAdmin):
    list_display = ('username', 'email', 'biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'qte_animais')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':( 'biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'qte_animais')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':( 'biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'qte_animais')}),
    )

admin.site.register(Pessoa, PessoaAdmin)