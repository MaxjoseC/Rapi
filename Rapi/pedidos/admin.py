from django.contrib import admin
from .models import Pedido
# Register your models here.
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'estado', 'total', 'fecha')
    list_filter = ('estado',)
    search_fields = ('cliente__nombre',)
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)
    list_per_page = 10