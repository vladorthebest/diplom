# Generated by Django 3.1.3 on 2021-05-18 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20210518_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson_e',
            name='nameg',
        ),
    ]