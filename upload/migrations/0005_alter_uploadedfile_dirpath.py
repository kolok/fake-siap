# Generated by Django 3.2.7 on 2021-10-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0004_auto_20211018_1351"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadedfile",
            name="dirpath",
            field=models.CharField(max_length=255, null=True),
        ),
    ]