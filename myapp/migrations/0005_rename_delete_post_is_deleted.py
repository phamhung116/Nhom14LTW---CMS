# Generated by Django 5.1 on 2024-09-11 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_topic_post_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='delete',
            new_name='is_deleted',
        ),
    ]
