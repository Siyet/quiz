# Generated by Django 2.1.4 on 2018-12-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_public',
            field=models.BooleanField(default=1, verbose_name='Опубликован?'),
            preserve_default=False,
        ),
    ]
