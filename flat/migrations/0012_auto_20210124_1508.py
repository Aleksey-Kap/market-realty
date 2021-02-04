# Generated by Django 3.1.3 on 2021-01-24 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0011_auto_20210124_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тип отопления(для выборки)',
                'verbose_name_plural': 'Тип отопления(для выборки)',
            },
        ),
        migrations.AddField(
            model_name='flat',
            name='heating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='flat.heating', verbose_name='Тип отопления'),
        ),
    ]