# Generated by Django 3.0.5 on 2020-04-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_postmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='playermodel',
            name='nikname',
            field=models.CharField(default='', max_length=100, verbose_name='Ник игрока'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='pub',
            field=models.BooleanField(default=True, verbose_name='Опубликован'),
        ),
    ]