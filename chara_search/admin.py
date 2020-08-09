from django.contrib import admin

from .models import Character,Stats

# Register your models here.
admin.site.register(Character)
admin.site.register(Stats)