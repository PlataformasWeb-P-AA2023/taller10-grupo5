# Generated by Django 4.2.2 on 2023-06-25 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('urbana', 'Urbana'), ('rural', 'Rural')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('nro_viviendas', models.IntegerField()),
                ('nro_parques', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])),
                ('nro_edificios', models.IntegerField()),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parroquias', to='ordenamiento.parroquia')),
            ],
        ),
    ]