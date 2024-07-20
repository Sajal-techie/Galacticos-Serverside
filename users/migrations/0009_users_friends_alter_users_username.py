# Generated by Django 5.0.6 on 2024-07-18 12:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_academy_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
