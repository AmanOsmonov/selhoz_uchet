# Generated by Django 4.2.3 on 2023-07-26 15:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pole', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('crop', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agriculture.crop')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriculture.farmer')),
                ('season', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agriculture.season')),
            ],
        ),
    ]