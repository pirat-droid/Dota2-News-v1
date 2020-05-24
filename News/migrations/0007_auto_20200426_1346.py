# Generated by Django 3.0.5 on 2020-04-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_auto_20200426_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countrymodel',
            options={'verbose_name': 'Старан', 'verbose_name_plural': 'Страны'},
        ),
        migrations.RemoveField(
            model_name='matchesmodel',
            name='percent1',
        ),
        migrations.RemoveField(
            model_name='matchesmodel',
            name='percent2',
        ),
        migrations.AddField(
            model_name='matchesmodel',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='Закончился'),
        ),
    ]
