# Generated by Django 3.1.5 on 2021-01-30 12:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20210130_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]