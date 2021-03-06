# Generated by Django 3.0.5 on 2020-04-26 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0005_auto_20200426_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название страны')),
                ('flag', models.ImageField(upload_to='flags/', verbose_name='Флаг')),
            ],
        ),
        migrations.AlterField(
            model_name='comandmodel',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='News.CountryModel'),
        ),
    ]
