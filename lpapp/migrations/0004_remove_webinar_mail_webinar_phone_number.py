# Generated by Django 5.1.3 on 2024-12-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpapp', '0003_rename_email_webinar_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webinar',
            name='mail',
        ),
        migrations.AddField(
            model_name='webinar',
            name='phone_number',
            field=models.CharField(default=9888, max_length=20),
            preserve_default=False,
        ),
    ]
