# Generated by Django 3.0 on 2019-12-08 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0022_auto_20191207_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('id',)},
        ),
    ]
