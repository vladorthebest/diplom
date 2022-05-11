# Generated by Django 3.1.3 on 2021-05-14 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('group', models.CharField(max_length=10)),
                ('number', models.PositiveIntegerField()),
                ('lesson', models.TextField()),
                ('teacher', models.TextField()),
                ('day', models.CharField(max_length=25)),
                ('zam', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Пара',
                'verbose_name_plural': 'Пары',
            },
        ),
    ]
