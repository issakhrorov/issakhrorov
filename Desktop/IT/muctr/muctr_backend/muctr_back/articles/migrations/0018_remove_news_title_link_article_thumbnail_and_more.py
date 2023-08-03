# Generated by Django 4.2.2 on 2023-07-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_rename_publised_at_news_news_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='title_link',
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='news_thumbnails'),
        ),
        migrations.AlterField(
            model_name='news',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='news_thumbnails'),
        ),
    ]
