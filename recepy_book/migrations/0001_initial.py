# Generated by Django 4.1.2 on 2022-10-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, null=True, verbose_name='Назва')),
                ('discription', models.CharField(default=None, max_length=400, null=True, verbose_name='Опис')),
                ('image', models.CharField(default=None, max_length=100, null=True, verbose_name='Фото')),
            ],
            options={
                'verbose_name_plural': 'Рецепти',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=50, null=True, verbose_name="Ім'я")),
                ('last_name', models.CharField(default=None, max_length=50, null=True, verbose_name='Прізвище')),
                ('username', models.CharField(default=None, max_length=30, null=True, verbose_name="Ім'я користувача")),
                ('register_name', models.CharField(default=None, max_length=255, null=True, verbose_name="Ім'я з анкети")),
                ('sex', models.CharField(default='', max_length=20, verbose_name='Стать')),
            ],
            options={
                'verbose_name_plural': 'Користувачі',
                'ordering': ['username'],
            },
        ),
    ]
