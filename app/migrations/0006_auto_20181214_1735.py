# Generated by Django 2.1.4 on 2018-12-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_category_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/', verbose_name='Картинка ответ'),
        ),
        migrations.AlterField(
            model_name='question',
            name='short_image',
            field=models.ImageField(blank=True, upload_to='media/images/', verbose_name='Картинка вопрос'),
        ),
    ]
