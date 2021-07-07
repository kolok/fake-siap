# Generated by Django 3.2.5 on 2021-07-06 16:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bailleurs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convention',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('numero', models.CharField(max_length=255)),
                ('date_fin_conventionnement', models.DateField()),
                ('financement', models.CharField(choices=[('PLUS', 'PLUS'), ('PLAI', 'PLAI'), ('PLUS-PLAI', 'PLUS-PLAI'), ('PLS', 'PLS')], default='PLUS', max_length=25)),
                ('soumis_le', models.DateTimeField()),
                ('valide_le', models.DateTimeField()),
                ('cree_le', models.DateTimeField(auto_now_add=True)),
                ('mis_a_jour_le', models.DateTimeField(auto_now=True)),
                ('bailleur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bailleurs.bailleur')),
            ],
        ),
        migrations.CreateModel(
            name='Pret',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('preteur', models.CharField(choices=[('ETAT', 'Etat'), ('EPCI', 'EPCI'), ('REGION', 'Region'), ('CDCF', 'Caisse des dépots et des consignations Froncière'), ('CDCL', 'Caisse des dépots et des consignations Locative'), ('AUTRE', 'Autre')], default='CDCF', max_length=25)),
                ('autre', models.CharField(max_length=255)),
                ('date_octroi', models.DateField()),
                ('numero', models.CharField(max_length=255)),
                ('duree', models.IntegerField()),
                ('montant', models.FloatField()),
                ('bailleur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bailleurs.bailleur')),
                ('convention', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conventions.convention')),
            ],
        ),
    ]