# Generated by Django 2.1.4 on 2018-12-14 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181213_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='isTrue',
            new_name='is_true',
        ),
    ]
