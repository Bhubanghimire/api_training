from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from products.models import Product
from products.serializers import ProductSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from accounts.permissions import AdminPermission, NormalUserPermission
from accounts.middleware import generate_access_token, generate_refresh_token
from rest_framework.permissions import  AllowAny

class ProductListAPI(APIView):
    
    
    def get(self, request):
        id = request.GET.get('id', False)
        if id:
            products = Product.objects.get(id=id)
            products_serializer = ProductSerializer(products).data
            return Response({"data":products_serializer})

        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True).data
        return Response({"data":products_serializer})
    

    def post(self, request):
        data = request.data

        
        products_serializer = ProductSerializer(data=data)
        if products_serializer.is_valid():
            products_serializer.save()
            print("valid")
            return Response({"data":products_serializer.data,"message":"Product added successfully."}, status=201)
        else:
            print("not valid", products_serializer.errors)
            return Response({"message":products_serializer.errors}, status=400)
        
    def put(self, request):
        data = request.data
        products_serializer = ProductSerializer(data=data)
        if products_serializer.is_valid():
            products_serializer.save()
            print("valid")
            return Response({"message":"Product added successfully."}, status=201)
        else:
            print("not valid", products_serializer.errors)
            return Response({"message":products_serializer.errors}, status=400)
        

    def delete(self, request):
        data = request.data['id']
        Product.objects.filter(id=data).delete()
        return Response({"message":"product deleted successfully"}, status=200)
        
        
        
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            jwt = {
                "access_token": generate_access_token(user),
                "refresh_token": generate_refresh_token(user)
            }
            return Response({"token":str(token.key), "jwt":jwt,"message":"login sucessful"}, status=200)
        else:
            return Response({"message":"wrong data"}, status=400)
