# Generated by Django 2.1.4 on 2018-12-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181214_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='games_num',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Отыграно раундов'),
        ),
        migrations.AlterField(
            model_name='team',
            name='points',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество очков'),
        ),
    ]
