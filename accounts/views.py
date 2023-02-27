from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from rest_framework import status

# Create your views here.
# class UserList(APIView):
#     def get(self, request):
#         return Response()

class UserAPI(APIView):
    def get(self, request):

        return
    
    def post(self, request):
        # sign up
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return
    
    def patch(self, request):
        # change user profile
        return

    def delete(self, request):
        #sign off
        return
