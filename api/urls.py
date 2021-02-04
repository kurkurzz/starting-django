from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.author, name='author'),
    path(r'news/', views.get_news_list, name='news list'),
    path(r'news/<str:pk>', views.get_news, name='news')
]
