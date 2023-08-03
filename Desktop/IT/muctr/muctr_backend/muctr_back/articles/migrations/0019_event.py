# Generated by Django 4.2.2 on 2023-08-01 05:54

import ckeditor_uploader.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_remove_news_title_link_article_thumbnail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('slider_photo', models.FileField(blank=True, null=True, upload_to='slider_photos')),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='events_thumbnails')),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('sort', models.IntegerField(default=1000)),
                ('status', models.CharField(choices=[('published', 'published'), ('draft', 'draft'), ('locked', 'locked'), ('deleted', 'deleted')], max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
