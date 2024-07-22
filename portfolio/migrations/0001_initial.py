# Generated by Django 4.2.2 on 2024-07-20 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='graphics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Graphics Portfolio',
            },
        ),
    ]
