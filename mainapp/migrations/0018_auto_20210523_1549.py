# Generated by Django 3.1.3 on 2021-05-23 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20210518_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='nameg',
        ),
        migrations.RemoveField(
            model_name='lesson_e',
            name='nameg',
        ),
        migrations.RemoveField(
            model_name='lesson_e',
            name='zam',
        ),
    ]
