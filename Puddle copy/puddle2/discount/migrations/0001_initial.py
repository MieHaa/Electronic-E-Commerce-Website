# Generated by Django 4.2.4 on 2023-11-20 04:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('percent', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Value must be greater than or equal to 0.'), django.core.validators.MaxValueValidator(100, message='Value must be less than or equal to 100.')])),
            ],
            options={
                'verbose_name_plural': 'Discounts',
                'ordering': ('code',),
            },
        ),
    ]