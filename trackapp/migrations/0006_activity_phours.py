# Generated by Django 3.1.3 on 2020-11-16 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackapp', '0005_auto_20201116_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='phours',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
    ]
