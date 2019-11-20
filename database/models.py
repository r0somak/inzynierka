from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Lekarz(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    specjalizacja = models.CharField(max_length=100, null=True)
    nr_pwz = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    telefon = models.CharField(max_length=100, null=True)


class Przychodnia(models.Model):
    nazwa = models.CharField(max_length=100)
    uica = models.CharField(max_length=100)
    nr_ulicy = models.CharField(max_length=100)
    nr_mieszkania = models.CharField(max_length=100, null=True)
    kod_pocztowy = models.CharField(max_length=100)
    miasto = models.CharField(max_length=100)
    wojewodztwo = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    telefon = models.CharField(max_length=100, null=True)
    lekarze = models.ManyToManyField(Lekarz)


def user_dir_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Dokument(models.Model):
    dokument = models.FileField(upload_to=user_dir_path)


class Pacjent(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    pesel = models.CharField(max_length=100)
    ulica = models.CharField(max_length=100)
    nr_ulicy = models.CharField(max_length=20)
    nr_mieszkania = models.CharField(max_length=20, null=True)
    kod_pocztowy = models.CharField(max_length=10)
    miasto = models.CharField(max_length=100)
    wojewodztwo = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    telefon = models.CharField(max_length=100, null=True)
    dokumenty = models.ManyToManyField(Dokument, null=True)


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


class Wizyta(models.Model):
    data_wizyty = models.DateTimeField()
    uwagi = models.CharField(max_length=500)

    fk_id_pacjent = models.ForeignKey(
        Pacjent,
        on_delete=models.CASCADE,
    )

    fk_id_lekarz = models.ForeignKey(
        Lekarz,
        on_delete=models.CASCADE,
    )

    fk_id_przychodnia = models.ForeignKey(
        Przychodnia,
        on_delete=models.CASCADE,
    )

    dokumenty = models.ManyToManyField(Dokument, null=True)
