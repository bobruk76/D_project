# Generated by Django 3.0.7 on 2020-07-15 14:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='Название породы')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='Кличка')),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(40)], verbose_name='Возраст')),
                ('photo', models.ImageField(blank=True, upload_to='pets_photo')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.Breed', verbose_name='Порода')),
            ],
        ),
    ]
