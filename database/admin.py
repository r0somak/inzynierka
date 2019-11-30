from django.contrib import admin
from .models import CustomUser, Pacjent
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Pacjent)
