# Generated by Django 3.1.3 on 2021-05-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210515_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='classroom',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
