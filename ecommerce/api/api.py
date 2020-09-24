from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import User,UserRole,Product,Order,OrderItem
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class userauth(ObtainAuthToken):
    def get(self, request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['User']
        token,created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class Userlist(APIView):

    def get(self,request):
        model = User.objects.all()
        serializer = userSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = userSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):

    def get_user(self,id):
        try:
            model = User.objects.get(id=id)
            return model
        except :
            return

    def get(self,request,id):
        if not self.get_user(id):
            return Response(f'User with id {id} not found in DB',status=status.HTTP_404_NOT_FOUND)
        serializer = userSerializer(self.get_user(id))
        return Response(serializer.data)

    def put(self,request,id):
        if not self.get_user(id):
            return Response(f'User with id {id} not found in DB',status=status.HTTP_404_NOT_FOUND)
        serializer = userSerializer(self.get_user(id), data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        if not self.get_user(id):
            return Response(f'User with id {id} not found in DB',status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(APIView):

    def get(self,request):
        model = Product.objects.all()
        serializer = productSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = productSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetails(APIView):

    def get_user(self,id):
        try:
            model = Product.objects.get(id=id)
            return model
        except :
            return

    def get(self,request,id):
        if not self.get_user(id):
            return Response(f'Product with id {id} not found in DB',status=status.HTTP_404_NOT_FOUND)
        serializer = productSerializer(self.get_user(id))
        return Response(serializer.data)

    def put(self,request,id):
        if not self.get_user(id):
            return Response(f'Product with id {id} not found in DB',status=status.HTTP_404_NOT_FOUND)
        serializer = productSerializer(self.get_user(id), data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        if not self.get_user(id):
            return Response(f'Product with id {id} not found in DB',status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderList(APIView):

    def get(self,request):
        model = Order.objects.all()
        serializer = orderSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = orderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class orderDetails(APIView):

    def get_user(self,id):
        try:
            model = Order.objects.get(order_id=id)
            return model
        except :
            return

    def get(self,request,id):
        if not self.get_user(id):
            return Response(f'Order with id {id} not found in DB',status=status.HTTP_404_NOT_FOUND)
        serializer = orderSerializer(self.get_user(id))
        return Response(serializer.data)

    def put(self,request,id):
        if not self.get_user(id):
            return Response(f'Order with id {id} not found in DB',status=status.HTTP_404_NOT_FOUND)
        serializer = orderSerializer(self.get_user(id), data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        if not self.get_user(id):
            return Response(f'Order with id {id} not found in DB',status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)