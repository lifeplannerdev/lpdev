# Generated by Django 5.1.3 on 2025-02-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpapp', '0020_remove_careers_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='careers',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
