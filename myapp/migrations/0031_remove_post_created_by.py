# Generated by Django 5.1 on 2024-09-17 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_alter_post_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
    ]
