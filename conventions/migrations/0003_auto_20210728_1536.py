# Generated by Django 3.2.5 on 2021-07-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conventions', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='date_fin_conventionnement',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='convention',
            name='soumis_le',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='convention',
            name='valide_le',
            field=models.DateTimeField(null=True),
        ),
    ]