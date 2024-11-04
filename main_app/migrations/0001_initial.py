# Generated by Django 5.1.2 on 2024-11-04 20:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('music_name', models.CharField(max_length=100)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.musician')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
