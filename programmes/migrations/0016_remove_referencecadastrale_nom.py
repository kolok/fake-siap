# Generated by Django 3.2.5 on 2021-09-14 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0015_auto_20210913_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referencecadastrale',
            name='nom',
        ),
    ]