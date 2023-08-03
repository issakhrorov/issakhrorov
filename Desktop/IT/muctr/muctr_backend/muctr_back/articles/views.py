from .models import Article, News, Widget, Course, Event
from django.contrib.auth.models import User, auth
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer, NewsSerializer, WidgetSerializer, CourseSerializer, EventSerializer
from django.contrib import messages
from django.shortcuts import render, redirect

@api_view(['GET'])
def getArticles(request):
  elements = Article.objects.all()
  serializer = ArticleSerializer(elements, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getNews(request):
  news = News.objects.all()
  serializer = NewsSerializer(news, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def getWidgets(request):
  widgets = Widget.objects.all()
  serializer = WidgetSerializer(widgets, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def getCourses(request):
  courses = Course.objects.all()
  serializer = CourseSerializer(courses, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def getParentArticles(request):
  parents = Article.objects.filter(parent=None)
  serializer = ArticleSerializer(parents, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def getEventArticles(request):
  serializer = EventSerializer(many=True)

  return Response(serializer.data)