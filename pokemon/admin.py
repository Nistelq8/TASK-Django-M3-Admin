from django.contrib import admin
from .models import Pokemon

# Register your models here.
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("id","name","hp","active")
    list_filter = ("active",)
    list_display_links = ("id","name")
fieldsets = (
        ('', {
            'fields': ('name', 'type', 'hp', 'active', 'created_at', 'models_at',),
        }),
        ('localization', {
            'classes': ('collapse',),
            'fields': ('name_fr', 'name_ar' ,'name_jp'),
        }),)
admin.site.register(Pokemon, PokemonAdmin)