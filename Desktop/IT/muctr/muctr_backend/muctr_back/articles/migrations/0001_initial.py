# Generated by Django 4.2.2 on 2023-06-15 06:36

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Химическая технология', 'Химическая технология'), ('Техносферная безопасность', 'Техносферная безопасность'), ('Материаловедение и технологии материалов', 'Материаловедение и технологии материалов'), ('Технология художественной обработки материалов', 'Технология художественной обработки материалов'), ('Наноматериалы', 'Наноматериалы')], max_length=50)),
                ('programs', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None)),
                ('level', models.CharField(choices=[('бакалавриат', 'бакалавриат'), ('магистратура', 'магистратура')], max_length=15)),
                ('duration', models.CharField(choices=[('2', 2), ('4', 4), ('4.6', 4.6)], max_length=3)),
                ('language', models.CharField(default='русский', max_length=10)),
                ('type', models.CharField(choices=[('очная', 'очная'), ('заочная', 'заочная')], max_length=10)),
                ('students_number', jsonfield.fields.JSONField()),
                ('fee', models.IntegerField()),
                ('doc_acceptance', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True, null=True), blank=True, null=True, size=None)),
                ('exam_days', models.DateField(blank=True, null=True)),
                ('appeal', models.DateField(blank=True, null=True)),
                ('admission_protocol', models.DateField(blank=True, null=True)),
                ('exam_scores', jsonfield.fields.JSONField()),
                ('exam_desc', models.TextField(blank=True, null=True)),
                ('required_docs', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None)),
                ('address', models.CharField(default='Мирзо-Улугбекский район, ТТЗ-1, дом 47, ауд. 111.', max_length=150)),
                ('additional_scores', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_link', models.CharField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.FileField(upload_to='news_thumbnails')),
                ('content', models.TextField(blank=True, null=True)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('sort', models.IntegerField(default=1000)),
                ('status', models.CharField(choices=[('published', 'published'), ('draft', 'draft'), ('locked', 'locked'), ('deleted', 'deleted')], max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publised_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Widgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='widget_thumbnails')),
                ('img', models.FileField(blank=True, null=True, upload_to='widget_imgs')),
                ('description', models.TextField(blank=True, null=True)),
                ('file', models.FileField(upload_to='widget_files')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_type', models.CharField(choices=[('text', 'text'), ('link', 'link'), ('download', 'download')], max_length=10)),
                ('title_link', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('sort', models.IntegerField(default=1000)),
                ('status', models.CharField(choices=[('published', 'published'), ('draft', 'draft'), ('locked', 'locked'), ('deleted', 'deleted')], max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publised_at', models.DateTimeField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
    ]
