# Generated by Django 3.1.3 on 2020-12-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0005_auto_20201216_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='isdayly',
            field=models.BooleanField(default=False, verbose_name='Посуточно аренда'),
        ),
        migrations.AddField(
            model_name='flat',
            name='isrent',
            field=models.BooleanField(default=False, verbose_name='Аренда'),
        ),
        migrations.AddField(
            model_name='flat',
            name='issale',
            field=models.BooleanField(default=False, verbose_name='Продажа'),
        ),
    ]