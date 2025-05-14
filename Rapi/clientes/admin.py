from django.contrib import admin
from .models import Cliente
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'direccion', 'descuentoBool')
    search_fields = ('nombre', 'telefono')
    list_filter = ('descuentoBool',)
    ordering = ('-id',)
    list_per_page = 10