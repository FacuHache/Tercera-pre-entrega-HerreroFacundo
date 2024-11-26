# Generated by Django 5.1.3 on 2024-11-27 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo_Titular2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'equipo titular',
                'verbose_name_plural': 'equipos titulares',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
            options={
                'verbose_name': 'fecha',
                'verbose_name_plural': 'fechas',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'jugador',
                'verbose_name_plural': 'jugadores',
                'ordering': ['nombre'],
            },
        ),
    ]
