# Generated by Django 3.1.3 on 2020-12-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0003_auto_20201214_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='coord_lat',
            field=models.CharField(max_length=100, null=True, verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='coord_long',
            field=models.CharField(max_length=100, null=True, verbose_name='долгота'),
        ),
    ]
