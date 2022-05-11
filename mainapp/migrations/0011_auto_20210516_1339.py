# Generated by Django 3.1.3 on 2021-05-16 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_name_group_group_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='groupid',
        ),
        migrations.AddField(
            model_name='lesson',
            name='categories',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='mainapp.name_group'),
            preserve_default=False,
        ),
    ]
