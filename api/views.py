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
def get_news_list(request):
    news = News.objects.all()
    serializer = NewsSerializer(news,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_news(request, pk):
    news = News.objects.get(id=pk)
    serializer = NewsSerializer(news,many=False)
    return Response(serializer.data)