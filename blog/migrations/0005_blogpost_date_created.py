# Generated by Django 3.2.7 on 2021-10-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
