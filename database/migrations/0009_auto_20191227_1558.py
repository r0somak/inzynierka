# Generated by Django 3.0 on 2019-12-27 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20191227_1302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daneepidemiologiczne',
            options={'ordering': ('data', 'dane_statystyczne__wojewodztwo')},
        ),
    ]
