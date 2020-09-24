from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *

def registration(request):
    if request.method == 'POST':
        serializer = registerSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Registerd new user'
            data['email'] = user.email
        else :
            data = serializer.errors
        return Response(data)


