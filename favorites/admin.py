from django.contrib import admin
from .models import Favorite

# Register your models here.
#TODO: Remove before prod deploy!!
admin.site.register(Favorite)