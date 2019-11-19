from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Lekarz(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    specjalizacja = models.CharField(max_length=100)
    nr_pwz = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=100)


class Pacjent(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    pesel = models.CharField(max_length=100)
    ulica = models.CharField(max_length=100)
    nr_ulicy = models.CharField(max_length=20)
    nr_mieszkania = models.CharField(max_length=20)
    kod_pocztowy = models.CharField(max_length=10)
    miasto = models.CharField(max_length=100)
    wojewodztwo = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=100)


class CustomUser(AbstractUser):
    fk_id_Lekarz = models.OneToOneField(
        Lekarz,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    fk_id_pacjent = models.OneToOneField(
        Pacjent,
        models.SET_NULL,
        blank=True,
        null=True,
    )
