# Generated by Django 4.2.4 on 2023-08-05 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Habilidades',
            new_name='Habilidad',
        ),
        migrations.RenameModel(
            old_name='Idiomas',
            new_name='Idioma',
        ),
    ]
