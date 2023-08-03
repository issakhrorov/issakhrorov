from django.urls import path
from . import views

urlpatterns = [
    path('articles', views.getArticles, name='get-articles'),
    path('widgets', views.getWidgets, name='get-widgets'),
    path('news', views.getNews, name='get-news'),
    path('courses', views.getCourses, name='get-courses'),
    path('parents', views.getParentArticles, name='get-parents'),
    path('events', views.getEventArticles, name='get-events'),


    # path('category/<str:pk>', views.getCategoryPromotions, name='categoryPromotions'),
    # path('category', views.getCategory, name='category'),
    # path('card/<str:pk>', views.getCards, name='card'),
    # path('info/<str:pk>', views.getInfo, name='info'),
    # path('rightvote/', views.rightvote, name="rightvote" ),
]
