# Generated by Django 5.1 on 2024-09-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_profile_avt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avt',
            field=models.ImageField(blank=True, default='default-user.png', null=True, upload_to='img'),
        ),
    ]