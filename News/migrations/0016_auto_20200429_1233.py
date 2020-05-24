# Generated by Django 3.0.5 on 2020-04-29 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0015_auto_20200429_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameArchivModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comand1_map', models.CharField(default='0', max_length=1, verbose_name='Выигранных карт 1 командой')),
                ('comand2_map', models.CharField(default='0', max_length=1, verbose_name='Выигранных карт 2 командой')),
                ('date', models.DateField(verbose_name='Дата проведения игры')),
                ('closed', models.BooleanField(default=False, verbose_name='Закончился')),
                ('comand1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comand_one', to='News.ComandModel')),
                ('comand2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comand_two', to='News.ComandModel')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='MatchesModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название матча')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип матча')),
            ],
            options={
                'verbose_name': 'Матч',
                'verbose_name_plural': 'Матчи',
            },
        ),
        migrations.DeleteModel(
            name='matchesModel',
        ),
        migrations.AddField(
            model_name='gamearchivmodel',
            name='name_match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='News.MatchesModule'),
        ),
        migrations.AddField(
            model_name='archivstreammodule',
            name='name_matches',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_name', to='News.MatchesModule'),
        ),
    ]