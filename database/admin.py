from django.contrib import admin
from .models import CustomUser, Pacjent, Lekarz, Wizyta, Przychodnia, Dokument, Objawy, JednostkaChorobowa, DaneStatystyczne, Badanie, DaneEpidemiologiczne
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Pacjent)
admin.site.register(Lekarz)
admin.site.register(Wizyta)
admin.site.register(Przychodnia)
admin.site.register(Dokument)
admin.site.register(Objawy)
admin.site.register(JednostkaChorobowa)
admin.site.register(DaneStatystyczne)
admin.site.register(DaneEpidemiologiczne)
admin.site.register(Badanie)
