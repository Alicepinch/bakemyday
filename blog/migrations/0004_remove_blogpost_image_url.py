# Generated by Django 3.2.7 on 2021-10-26 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211025_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='image_url',
        ),
    ]