# Generated by Django 4.2.7 on 2023-11-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_content_title_content_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
