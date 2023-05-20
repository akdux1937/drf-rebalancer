# Generated by Django 4.0.5 on 2023-05-20 02:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountPosition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ticker', models.CharField(max_length=25)),
                ('shares', models.DecimalField(decimal_places=4, max_digits=13)),
            ],
        ),
    ]
