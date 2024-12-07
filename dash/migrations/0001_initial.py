# Generated by Django 5.1.4 on 2024-12-06 17:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(13)])),
                ('sex', models.PositiveBigIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True)),
                ('height', models.PositiveSmallIntegerField(null=True)),
                ('predictions', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
