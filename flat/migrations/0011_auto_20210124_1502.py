# Generated by Django 3.1.3 on 2021-01-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0010_auto_20210124_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='entrances',
            field=models.IntegerField(blank=True, null=True, verbose_name='Подъезды'),
        ),
        migrations.DeleteModel(
            name='Entrances',
        ),
    ]
