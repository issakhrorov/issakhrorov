from rest_framework.serializers import ModelSerializer
from .models import Article, News, Widget, Course, Event

class ArticleSerializer(ModelSerializer):
  class Meta:
    model = Article
    fields = '__all__'

class NewsSerializer(ModelSerializer):
  class Meta:
    model = News 
    fields = '__all__'

class WidgetSerializer(ModelSerializer):
  class Meta: 
    model = Widget
    fields = '__all__'

class CourseSerializer(ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'

class EventSerializer(ModelSerializer):
  class Meta:
    model = Event
    fields = '__all__'