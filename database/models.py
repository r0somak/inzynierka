import datetime

from operator import itemgetter

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
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    specjalizacja = models.CharField(max_length=100, null=True, default='BRAK')
    nr_pwz = models.CharField(max_length=100, null=True)
    telefon = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        id_string = str(self.id) + u': ' + self.name + ' ' + self.surname + ', ' + self.specjalizacja
        return id_string


class Przychodnia(models.Model):
    nazwa = models.CharField(max_length=100, blank=True)
    ulica = models.CharField(max_length=100, blank=True)
    nr_ulicy = models.CharField(max_length=100, blank=True)
    nr_mieszkania = models.CharField(max_length=100, blank=True)
    kod_pocztowy = models.CharField(max_length=100, blank=True)
    miasto = models.CharField(max_length=100, blank=True)
    wojewodztwo = models.CharField(
        max_length=30,
        choices=WOJEWODZTWO,
        default='BRAK',
    )
    email = models.CharField(max_length=100, blank=True)
    telefon = models.CharField(max_length=100, blank=True)
    lekarze = models.ManyToManyField(Lekarz)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        id_string = str(self.id) + u': ' + self.nazwa + u', ' + self.wojewodztwo + u', ' + self.miasto
        return id_string


def user_dir_path(instance, filename):
    return 'user_{0}/'.format(instance)


class Dokument(models.Model):
    data_dodania = models.DateTimeField(default=datetime.datetime.now)
    dokument = models.FileField(upload_to=user_dir_path)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        id_string = str(self.id) + u': ' + str(self.dokument)
        return id_string


class Pacjent(models.Model):
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    pesel = models.CharField(max_length=100, blank=True)
    ulica = models.CharField(max_length=100, blank=True)
    nr_ulicy = models.CharField(max_length=20, blank=True)
    nr_mieszkania = models.CharField(max_length=20, blank=True)
    kod_pocztowy = models.CharField(max_length=10, blank=True)
    miasto = models.CharField(max_length=100, blank=True)
    wojewodztwo = models.CharField(
        max_length=30,
        choices=WOJEWODZTWO,
        default='BRAK',
    )
    telefon = models.CharField(max_length=100, blank=True)
    dokumenty = models.ForeignKey(
        Dokument,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ('id', )

    def __str__(self):
        id_string = str(self.id) + u': ' + self.name + u' ' + self.surname
        return id_string


class Administrator(models.Model):
    name = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    fk_id_lekarz = models.OneToOneField(
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

    class Meta:
        ordering = ('id', )

    def __str__(self):
        id_string = str(self.id) + u': ' + self.username + u', ' + self.email
        return id_string


class Objawy(models.Model):
    nazwa = models.CharField(max_length=250)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        id_string = str(self.id) + u': ' + self.nazwa
        return id_string


class DaneStatystyczne(models.Model):
    wojewodztwo = models.CharField(
        max_length=100,
        choices=WOJEWODZTWO,
        default='BRAK',
    )
    liczba_ludnosci = models.BigIntegerField()

    class Meta:
        ordering = ('id', )

    def __str__(self):
        id_string = str(self.id) + u': ' + self.wojewodztwo + u', ludność: ' + str(self.liczba_ludnosci)
        return id_string


class JednostkaChorobowa(models.Model):
    nazwa = models.CharField(max_length=200, blank=True)
    opis = models.CharField(max_length=500, blank=True)
    nr_icd = models.CharField(max_length=100, blank=True)
    objawy = models.ManyToManyField(Objawy)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        id_string = str(self.id) + u': ' + self.nazwa + u', ' + self.nr_icd
        return id_string


class DaneEpidemiologiczne(models.Model):
    jednostka_chorobowa = models.ForeignKey(
        JednostkaChorobowa,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    dane_statystyczne = models.ForeignKey(
        DaneStatystyczne,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    data = models.DateField(null=True)
    liczba_zachorowan = models.BigIntegerField()
    prewalencja = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('data', 'dane_statystyczne__wojewodztwo', 'jednostka_chorobowa__nazwa', )

    def __str__(self):
        id_string = str(self.data.year) + u', ' + self.dane_statystyczne.wojewodztwo + u', ' + self.jednostka_chorobowa.nazwa
        return id_string

    def get_prevalence(self):
        return str((self.liczba_zachorowan / self.dane_statystyczne.liczba_ludnosci)*100)[:5]


class Badanie(models.Model):
    nazwa = models.CharField(max_length=200)


class Wizyta(models.Model):
    data_wizyty = models.DateTimeField()
    uwagi = models.CharField(max_length=500, blank=True)

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
    dokumenty = models.ManyToManyField(Dokument, blank=True)
    objawy = models.ManyToManyField(Objawy, blank=True)
    badania = models.ManyToManyField(Badanie, blank=True)
    diagnoza = models.ForeignKey(
        JednostkaChorobowa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('id', )
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'data_wizyty',
                    'fk_id_lekarz',
                    'fk_id_pacjent',
                ],
                name='Unikatowosc wizyty'
            )
        ]

    def __str__(self):
        id_string = str(self.id) + u': ' + str(self.data_wizyty) + u', pacjent: ' + str(self.fk_id_pacjent)
        return id_string

    def get_probability(self):
        choroby = JednostkaChorobowa.objects.get_queryset()
        objawy_pacjenta = self.objawy.get_queryset()
        dane_stat = DaneEpidemiologiczne.objects.get_queryset()
        wynik = []
        now = datetime.datetime.now()
        wojewodztwo = self.fk_id_przychodnia.wojewodztwo
        for choroba in choroby:
            dd = dane_stat.get(jednostka_chorobowa=choroba.id, data__year=now.year, dane_statystyczne__wojewodztwo=wojewodztwo)
            objawy_choroby = choroba.objawy.get_queryset()
            liczba_wspolnych_objawow = len(set(objawy_pacjenta).intersection(objawy_choroby))
            liczba_objawow_choroby = len(objawy_choroby)
            pokrycie = str((liczba_wspolnych_objawow / liczba_objawow_choroby)*100)[:5]
            wynik.append({"pokrycie": pokrycie, "nazwa": choroba.nazwa, "prewalencja": dd.get_prevalence()})

        dane = sorted(wynik, key=lambda x: x['pokrycie'], reverse=True)
        return dane[:5]

