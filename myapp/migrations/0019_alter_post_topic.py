# Generated by Django 5.1 on 2024-09-13 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_rename_created_date_comment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(blank=True, default='Thường Ngày', null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.topic'),
        ),
    ]
