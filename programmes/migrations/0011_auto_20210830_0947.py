# Generated by Django 3.2.5 on 2021-08-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0010_alter_programme_type_operation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programme',
            name='nb_logement_non_conventionne',
        ),
        migrations.AddField(
            model_name='programme',
            name='autre_locaux_hors_convention',
            field=models.TextField(null=True),
        ),
    ]