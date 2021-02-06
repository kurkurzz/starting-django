from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import NewsSerializer
from .models import News

#function based view
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
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def news_details(request, id):
    try:
        news = News.objects.get(id=id)
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
    except:
        return HttpResponse(status.HTTP_404_NOT_FOUND)

#class based view
class NewsAPIView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class NewsDetailsAPIView(APIView):
    def get_news(self, id):
        try:
            return News.objects.get(id=id)
        except:
            return HttpResponse(status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        news = self.get_news(id)
        if type(news) is HttpResponse:
            return news
        serializer = NewsSerializer(news)
        return Response(serializer.data,status.HTTP_200_OK)

    def put(self, request, id):
        news = self.get_news(id)
        if type(news) is HttpResponse:
            return news
        serializer = NewsSerializer(news,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        news = self.get_news(id)
        if type(news) is HttpResponse:
            return news
        news.delete()
        return Response(status.HTTP_204_NO_CONTENT)