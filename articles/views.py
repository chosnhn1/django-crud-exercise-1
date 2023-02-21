from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article
from articles.serializers import ArticleSerializer, CommentSerializer
from rest_framework import status

# Create your views here.
class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.order_by('-pk')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        context = request.data
        serializer = ArticleSerializer(data=context)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    