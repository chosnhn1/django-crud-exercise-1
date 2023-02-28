from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from rest_framework import status
from accounts.models import User


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
    
    def patch(self, request, pk):
        user = get_object_or_404(User, pk=request.pk)
        serializer = UserSerializer(user, data=request.data)
        if request.user.pk == pk or request.user.is_admin:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # change user profile
        return

    def delete(self, request, pk):
        sign_off_user = get_object_or_404(User, pk=request.user.pk)
        if request.user.pk == pk or request.user.is_admin:
            sign_off_user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
