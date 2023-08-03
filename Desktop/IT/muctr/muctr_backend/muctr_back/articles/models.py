from django.db import models
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField

TITLE_TYPE = (
    ('text', 'text'),
    ('link', 'link'),
    ('download', 'download')
)

STATUS = (
    ('published', 'published'),
    ('draft', 'draft'),
    ('locked', 'locked'),
    ('deleted', 'deleted')
)

WIDGET_NAME = (
    ('top_menu', 'top_menu'),
    ('study', 'study'),
    ('strengths', 'strengths'),
    ('courses', 'courses'),
)

COURSES = (
    ('Химическая технология', 'Химическая технология'),
    ('Техносферная безопасность', 'Техносферная безопасность'),
    ('Материаловедение и технологии материалов', 'Материаловедение и технологии материалов'),
    ('Технология художественной обработки материалов', 'Технология художественной обработки материалов'),
    ('Наноматериалы', 'Наноматериалы')
)

COURSE_LEVELS = (
    ('бакалавриат', 'бакалавриат'),
    ('магистратура', 'магистратура'),
)

COURSE_DURATION = (
    ('2', 2),
    ('4', 4),
    ('4.6', 4.6),
)

COURSE_TYPE = (
    ('очная', 'очная'),
    ('заочная', 'заочная')
)


class Article(models.Model):
    title = models.CharField(max_length=200)
    title_type = models.CharField(max_length=10, choices=TITLE_TYPE)
    title_link = models.CharField(max_length=255, null=True, blank=True)
    thumbnail = models.FileField(upload_to='news_thumbnails', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    excerpt = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=255 ,null=True, blank=True)
    sort = models.IntegerField(default=1000)
    status = models.CharField(max_length=15, choices=STATUS)
    description = models.TextField(null=True, blank=True)
    keywords = ArrayField(models.CharField(max_length=200, null=True, blank=True),default=list, size=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class News(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    thumbnail = models.FileField(upload_to='news_thumbnails', null=True, blank=True)
    excerpt = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=255 ,null=True, blank=True)
    sort = models.IntegerField(default=1000)
    status = models.CharField(max_length=15, choices=STATUS)
    description = models.TextField(null=True, blank=True)
    keywords = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    news_date = models.DateTimeField(null=True, blank=True)

class Event(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    slider_photo = models.FileField(upload_to='slider_photos', null=True, blank=True)
    thumbnail = models.FileField(upload_to='events_thumbnails', null=True, blank=True)
    excerpt = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=255 ,null=True, blank=True)
    sort = models.IntegerField(default=1000)
    status = models.CharField(max_length=15, choices=STATUS)
    description = models.TextField(null=True, blank=True)
    keywords = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField(null=True, blank=True)

class Widget(models.Model):
    name = models.CharField(choices=WIDGET_NAME),
    title = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.FileField(upload_to='widget_thumbnails', null=True, blank=True)
    img = models.FileField(upload_to='widget_imgs', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='widget_files')
    file_link = models.CharField(max_length=200, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)

class Course(models.Model):
    name = models.CharField(choices=COURSES, max_length=50)
    programs = ArrayField(models.CharField(max_length=255), null=True, blank=True)       
    level = models.CharField(choices=COURSE_LEVELS, max_length=15)
    duration = models.CharField(choices=COURSE_DURATION, max_length=3)
    language = models.CharField(max_length=10, default='русский')
    type = models.CharField(choices=COURSE_TYPE, max_length=10)
    students_number = models.JSONField()
    fee = models.IntegerField()
    doc_acceptance = ArrayField(models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True), null=True, blank=True)       
    exam_days = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    appeal = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    admission_protocol = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    exam_scores = models.JSONField()
    exam_desc = models.TextField(blank=True, null=True)
    required_docs = ArrayField(models.CharField(max_length=255), null=True, blank=True)       
    address = models.CharField(max_length=150, default='Мирзо-Улугбекский район, ТТЗ-1, дом 47, ауд. 111.')
    additional_scores = models.JSONField(default=dict)