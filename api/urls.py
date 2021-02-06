from django.urls import path
from . import views 

urlpatterns = [
    path(r'', views.author, name='author'),
    #function based view
    # path(r'news/', views.news, name='news'),
    # path(r'news/<str:id>', views.news_details, name='news detail'),
    #class based view
    path(r'news/', views.NewsAPIView.as_view(), name='news'),
    path(r'news/<str:id>', views.NewsDetailsAPIView.as_view(), name='news detail'),
]
