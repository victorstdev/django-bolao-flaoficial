from django.contrib import admin
from .models import Evento, Lutador, Luta, Card, Resultado
# Register your models here.

class LutaInline(admin.TabularInline):
    model = Luta
    extra = 0
    raw_id_fields = ('lutadorA', 'lutadorB')

class ResultadoInline(admin.TabularInline):
    model = Resultado
    extra = 0

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data')
    list_filter = ['data']
    inlines = [LutaInline]

@admin.register(Lutador)
class LutadorAdmin(admin.ModelAdmin):
    list_display = ('sobrenome', 'nome', 'apelido')
    search_fields = ('nome', 'sobrenome', 'apelido')
    

@admin.register(Luta)
class LutaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'evento')
    inlines = [ResultadoInline]

admin.site.register(Card)