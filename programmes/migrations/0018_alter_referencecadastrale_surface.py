# Generated by Django 3.2.5 on 2021-09-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programmes", "0017_auto_20210914_1644"),
    ]

    operations = [
        migrations.AlterField(
            model_name="referencecadastrale",
            name="surface",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
