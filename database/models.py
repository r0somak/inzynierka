from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

WOJEWODZTWO = [
    ('BRAK', u'Brak'),
    ('DOLNOSLAKIE', u'Dolnośląskie'),
    ('KUJAWSKOPOMORSKIE', u'Kujawsko-pomorskie'),
    ('LUBELSKIE', u'Lubelskie'),
    ('LUBUSKIE', u'Lubuskie'),
    ('LODZKIE', u'Łódzkie'),
    ('MALOPOLSKIE', u'Małopolskie'),
    ('MAZOWIECKIE', u'Mazowieckie'),
    ('OPOLSKIE', u'Opolskie'),
    ('PODKARPACKIE', u'Podkarpackie'),
    ('PODLASKIE', u'Podlaskie'),
    ('POMORSKIE', u'Pomorskie'),
    ('SLASKIE', u'Śląskie'),
    ('SWIETOKRZYSKIE', u'Świętokrzyskie'),
    ('WARMINSKOMAZURSKIE', u'Warmińsko-mazurskie'),
    ('WIELKOPOLSKIE', u'Wielkopolskie'),
    ('ZACHODNIOPOMORSKIE', u'Zachodniopomorskie'),
]

class Lekarz(models.Model):
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    specjalizacja = models.CharField(max_length=100, null=True)
    nr_pwz = models.CharField(max_length=100, null=True)
    telefon = models.CharField(max_length=100, null=True)


class Przychodnia(models.Model):
    nazwa = models.CharField(max_length=100)
    uica = models.CharField(max_length=100)
    nr_ulicy = models.CharField(max_length=100)
    nr_mieszkania = models.CharField(max_length=100, null=True)
    kod_pocztowy = models.CharField(max_length=100)
    miasto = models.CharField(max_length=100)
    wojewodztwo = models.CharField(
        max_length=30,
        choices=WOJEWODZTWO,
        default='BRAK',
    )
    email = models.CharField(max_length=100, null=True)
    telefon = models.CharField(max_length=100, null=True)
    lekarze = models.ManyToManyField(Lekarz)


def user_dir_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Dokument(models.Model):
    dokument = models.FileField(upload_to=user_dir_path)


class Pacjent(models.Model):
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    pesel = models.CharField(max_length=100, null=True)
    ulica = models.CharField(max_length=100, null=True)
    nr_ulicy = models.CharField(max_length=20, null=True)
    nr_mieszkania = models.CharField(max_length=20, null=True)
    kod_pocztowy = models.CharField(max_length=10, null=True)
    miasto = models.CharField(max_length=100, null=True)
    wojewodztwo = models.CharField(
        max_length=30,
        choices=WOJEWODZTWO,
        default='BRAK',
    )
    telefon = models.CharField(max_length=100, null=True)
    dokumenty = models.ForeignKey(
        Dokument,
        null=True,
        on_delete=models.CASCADE
    )


class Administrator(models.Model):
    name = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=200, unique=True)
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

    fk_id_admin = models.OneToOneField(
        Administrator,
        models.SET_NULL,
        blank=True,
        null=True,
    )


class Objawy(models.Model):
    nazwa = models.CharField(max_length=250)


class JednostkaChorobowa(models.Model):
    opis = models.CharField(max_length=500)
    nr_icd = models.CharField(max_length=100)
    objawy = models.ManyToManyField(Objawy)


class DaneStatystyczne(models.Model):
    wojewodztwo = models.CharField(max_length=100)
    liczba_zachorowan = models.BigIntegerField()
    choroba = models.ManyToManyField(JednostkaChorobowa)


class Badanie(models.Model):
    nazwa = models.CharField(max_length=200)


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
    dokumenty = models.ManyToManyField(Dokument)
    objawy = models.ManyToManyField(Objawy)
    badania = models.ManyToManyField(Badanie)
