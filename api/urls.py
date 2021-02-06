from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.author, name='author'),
    path(r'news/', views.news, name='news'),
    path(r'news/<str:pk>', views.news_details, name='news detail'),
]
