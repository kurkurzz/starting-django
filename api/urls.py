from django.urls import path
from . import views

urlpatterns = [
    path('', views.author, name='author'),
    path('news/', views.get_news, name='news')
]
