# Generated by Django 3.0.5 on 2020-04-26 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComandModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя команды')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип команды')),
                ('country', models.CharField(max_length=50, verbose_name='Старна')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя игрока')),
                ('photo', models.ImageField(upload_to='players/', verbose_name='Фото игрока')),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название поста')),
                ('text', models.TextField(verbose_name='Текст поста')),
                ('date', models.DateField()),
                ('top', models.BooleanField(default=False, verbose_name='Главнй пост')),
                ('publick', models.BooleanField(default=True, verbose_name='Опубликовать')),
            ],
        ),
        migrations.CreateModel(
            name='ReitingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.SmallIntegerField(default=0, verbose_name='Место команды')),
                ('reiting', models.SmallIntegerField(default=0, verbose_name='Рейтинг команды')),
                ('date', models.DateField()),
                ('comand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='News.ComandModel')),
            ],
        ),
        migrations.CreateModel(
            name='matchesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent1', models.CharField(max_length=4, verbose_name='Процент за 1-ую команду')),
                ('percent2', models.CharField(max_length=4, verbose_name='Процент за 2-ую команду')),
                ('comand1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comand_one', to='News.ComandModel')),
                ('comand2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comand_two', to='News.ComandModel')),
            ],
        ),
        migrations.AddField(
            model_name='comandmodel',
            name='player',
            field=models.ManyToManyField(related_name='player_comand', to='News.PlayerModel', verbose_name='игрок'),
        ),
    ]