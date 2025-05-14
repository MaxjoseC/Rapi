from django.contrib import admin
from .models import Item
# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'slug')
    search_fields = ('nombre',)
    list_filter = ('stock',)
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ('-id',)
    list_per_page = 10