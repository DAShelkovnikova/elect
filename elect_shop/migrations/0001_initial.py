# Generated by Django 5.1.5 on 2025-01-27 08:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualEntrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('country', models.CharField(max_length=255, verbose_name='страна')),
                ('city', models.CharField(max_length=255, verbose_name='город')),
                ('street', models.CharField(max_length=255, verbose_name='улица')),
                ('house_number', models.CharField(max_length=20, verbose_name='номер дома')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('level', models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)], verbose_name='уровень в иерархии')),
            ],
            options={
                'verbose_name': 'индивидуальный предприниматель',
                'verbose_name_plural': 'индивидуальные предприниматели',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('country', models.CharField(max_length=255, verbose_name='страна')),
                ('city', models.CharField(max_length=255, verbose_name='город')),
                ('street', models.CharField(max_length=255, verbose_name='улица')),
                ('house_number', models.CharField(max_length=20, verbose_name='номер дома')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0)], verbose_name='уровень в иерархии')),
            ],
            options={
                'verbose_name': 'производитель',
                'verbose_name_plural': 'производители',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('model', models.CharField(max_length=255, verbose_name='модель')),
                ('release_date', models.DateField(verbose_name='дата выхода на рынок')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
        migrations.CreateModel(
            name='RetailNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('country', models.CharField(max_length=255, verbose_name='страна')),
                ('city', models.CharField(max_length=255, verbose_name='город')),
                ('street', models.CharField(max_length=255, verbose_name='улица')),
                ('house_number', models.CharField(max_length=20, verbose_name='номер дома')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('level', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)], verbose_name='уровень в иерархии')),
            ],
            options={
                'verbose_name': 'розничная сеть',
                'verbose_name_plural': 'розничные сети',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='количество')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='долг')),
            ],
            options={
                'verbose_name': 'транзакция',
                'verbose_name_plural': 'транзакции',
            },
        ),
    ]
