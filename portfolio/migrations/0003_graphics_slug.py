# Generated by Django 4.2.2 on 2024-07-21 00:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_graphics_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphics',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
            preserve_default=False,
        ),
    ]
