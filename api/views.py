from django.shortcuts import render
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NewsSerializer
from .models import News

# Create your views here.
@api_view(['GET'])
def author(request):
    author = {
        'Name' : 'Muhammad Nurhafiz',
        'Github Link' : 'https://github.com/kurkurzz'
    }
    return Response(author)

@api_view(['GET'])
def get_news(request):
    news = News.objects.all()
    print(news)
    serializer = NewsSerializer(news,many=True)
    return Response(serializer.data)