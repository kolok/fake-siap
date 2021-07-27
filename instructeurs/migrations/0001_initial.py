# Generated by Django 3.2.5 on 2021-07-23 10:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('nom', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
        ),
    ]
