# Generated by Django 5.1 on 2024-09-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_remove_post_end_date_remove_post_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
