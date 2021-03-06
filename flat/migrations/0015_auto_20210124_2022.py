# Generated by Django 3.1.3 on 2021-01-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0014_flat_garbagechute'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='bath',
            field=models.BooleanField(blank=True, null=True, verbose_name='Ванна'),
        ),
        migrations.AddField(
            model_name='flat',
            name='conditioner',
            field=models.BooleanField(blank=True, null=True, verbose_name='Кондиционер'),
        ),
        migrations.AddField(
            model_name='flat',
            name='dishwasher',
            field=models.BooleanField(blank=True, null=True, verbose_name='Посудомоечная машина'),
        ),
        migrations.AddField(
            model_name='flat',
            name='fridge',
            field=models.BooleanField(blank=True, null=True, verbose_name='Холодильник'),
        ),
        migrations.AddField(
            model_name='flat',
            name='furnitureintherooms',
            field=models.BooleanField(blank=True, null=True, verbose_name='Мебель в комнатах'),
        ),
        migrations.AddField(
            model_name='flat',
            name='internet',
            field=models.BooleanField(blank=True, null=True, verbose_name='Интернет'),
        ),
        migrations.AddField(
            model_name='flat',
            name='showercabin',
            field=models.BooleanField(blank=True, null=True, verbose_name='Душевая кабина'),
        ),
        migrations.AddField(
            model_name='flat',
            name='telephone',
            field=models.BooleanField(blank=True, null=True, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='flat',
            name='thefurnitureinthekitchen',
            field=models.BooleanField(blank=True, null=True, verbose_name='Мебель на кухне'),
        ),
        migrations.AddField(
            model_name='flat',
            name='tv',
            field=models.BooleanField(blank=True, null=True, verbose_name='Телевизор'),
        ),
        migrations.AddField(
            model_name='flat',
            name='washingmachine',
            field=models.BooleanField(blank=True, null=True, verbose_name='Стиральная машина'),
        ),
        migrations.AddField(
            model_name='flat',
            name='withanimals',
            field=models.BooleanField(blank=True, null=True, verbose_name='Можно с животными'),
        ),
        migrations.AddField(
            model_name='flat',
            name='withchildren',
            field=models.BooleanField(blank=True, null=True, verbose_name='Можно с детьми'),
        ),
    ]
