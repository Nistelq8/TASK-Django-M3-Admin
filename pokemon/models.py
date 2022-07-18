from datetime import datetime
from queue import Empty
from unicodedata import name
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.
class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
        WATER = 'WA', ('Water')
        GRASS = 'GR', ('Grass')
        GHOST = 'GH', ('Ghost')
        STEEL = 'ST', ('Steel')
        FAIRY = 'FA', ('Fairy')
    name = models.CharField(max_length=30)
    type =  models.CharField(max_length=2,choices=PokemonType.choices)
    hp = models.PositiveIntegerField(default=True)
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30,default=Empty)
    name_ar = models.CharField(max_length=30,default=Empty)
    name_jp = models.CharField(max_length=30,default=Empty)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
