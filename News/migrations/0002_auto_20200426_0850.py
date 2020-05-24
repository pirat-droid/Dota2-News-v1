# Generated by Django 3.0.5 on 2020-04-26 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comandmodel',
            options={'verbose_name': 'Команда', 'verbose_name_plural': 'Команды'},
        ),
        migrations.AlterModelOptions(
            name='matchesmodel',
            options={'verbose_name': 'Матч', 'verbose_name_plural': 'Матчи'},
        ),
        migrations.AlterModelOptions(
            name='playermodel',
            options={'verbose_name': 'Игрок', 'verbose_name_plural': 'Игроки'},
        ),
        migrations.AlterModelOptions(
            name='postmodel',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='reitingmodel',
            options={'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинги'},
        ),
        migrations.RenameField(
            model_name='postmodel',
            old_name='publick',
            new_name='pub',
        ),
    ]
