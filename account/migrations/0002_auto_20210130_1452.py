# Generated by Django 3.1.5 on 2021-01-30 12:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='like',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='more_user_info',
            name='profile_photo',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
    ]