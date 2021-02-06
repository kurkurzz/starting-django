
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import NewsSerializer
from .models import News

# Create your views here.
@api_view(['GET'])
def author(request):
    main = {
        'author':
            {
            'name' : 'Muhammad Nurhafiz',
            'github link' : 'https://github.com/kurkurzz'
            },
        'content' : {
            '/api/news' : '''['GET','POST']''',
            '/api/news/{id}' : '''['GET','PUT','DELETE']'''
        }
    }
    return Response(main)

@api_view(['GET','POST'])
def news(request):
    if request.method=='GET':
        news = News.objects.all()
        serializer = NewsSerializer(news,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def news_details(request, pk):
    news = News.objects.get(id=pk)
    if request.method=='GET':
        serializer = NewsSerializer(news)
        return Response(serializer.data,status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = NewsSerializer(news,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        news.delete()
        return Response(status.HTTP_204_NO_CONTENT)