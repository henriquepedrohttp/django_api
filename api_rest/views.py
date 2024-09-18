from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

# Create your views here.
@api_view(['GET'])
def get_users(request):
  
  if request.method == 'GET':
    
    users = User.objects.all()
    
    serializer = UserSerializer(users,many=True)
    
    return Response(serializer.data)
  
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request,nick):
  try:
    user = User.objects.get(pk=nick)
    serializer = UserSerializer(user)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  return Response(serializer.data)
  