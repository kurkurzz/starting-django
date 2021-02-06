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
        'name' : 'Muhammad Nurhafiz',
        'github link' : 'https://github.com/kurkurzz'
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

@api_view(['POST'])
def create_news(request):
    serializer = NewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)