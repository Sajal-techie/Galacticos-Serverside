# Generated by Django 5.0.6 on 2024-06-04 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_cover_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='academy',
            name='is_certified',
            field=models.BooleanField(default=False),
        ),
    ]
