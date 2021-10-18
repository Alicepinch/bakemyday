# Generated by Django 3.2.7 on 2021-10-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_preview',
            field=models.CharField(blank=True, max_length=260, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blog_title',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image_url',
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
    ]
