from django.contrib import admin
from .models import CustomUser, Pacjent, Lekarz, Wizyta
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Pacjent)
admin.site.register(Lekarz)
admin.site.register(Wizyta)
