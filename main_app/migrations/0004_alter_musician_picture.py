# Generated by Django 5.1.2 on 2024-11-06 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_musician_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
