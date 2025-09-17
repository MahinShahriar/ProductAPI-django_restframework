from rest_framework.response import Response
from rest_framework.viewsets import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.cache import cache
from .models import Product
from .serializer import ProductSerializer, SellerSerializer, SellerRegistrationSerializer, SellerLoginSerializer


# THIS PAGE WILL SHOW THE ENDPOINTS
@api_view(['GET'])
def product_overview(request):
    product_urls = {
            'List': '/list',
            'Detail': '/detail/<id>  (example: /product/detail/21)',
            'Create': '/create   ( Login Required !)',
            'Update': '/update/<id>     ( Login Required !)',
            'Delete': '/delete/<id>     ( Login Required !)'
    }

    return Response(product_urls)


# PRODUCT LIST
@api_view(['GET'])
def product_list(request):
    product = cache.get('all_products')
    if not product:
        print('From Database !')
        product = Product.objects.all()
        cache.set('all_products', product, timeout=60*15)
    elif product:
        print("cache found ! ")
    serialized = ProductSerializer(product, many=True)
    return Response(serialized.data)


# DETAIL OF SPECIFIC PRODUCT
@api_view(['GET'])
def product_detail(request, pk):
    product = cache.get(f"product_{pk}")
    if not product:
        print('From Database !')
        product = Product.objects.get(pk=pk)
        cache.set(f'product_{pk}', product, timeout=60*15)
    elif product:
        print("cache found ! ")
    serialized = ProductSerializer(product, many=False)

    return Response(serialized.data)


# CREATE PRODUCT ( AUTHENTICATION REQUIRED)
class CreateProductView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer


# UPDATE A SPECIFIC PRODUCT (AUTHENTICATION REQUIRED)
class UpdateProducView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


# DELETE A SPECIFIC PRODUCT ( AUTHENTICATION REQUIRED)
@api_view(['DELETE'])
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()

    return Response("Item Successfully Deleted !")


# IT WILL SHOW PRODUCT LIST OF A SPECIFIC SELLER.
@api_view(['GET'])
def seller_product(request, pk):
    products = Product.objects.filter(seller=pk)
    seller = User.objects.get(pk=pk)
    serialized = ProductSerializer(products, many=True)

    return Response({'Seller': seller.name, 'Products': serialized.data})


# SELLER REGISTRATION
class SellerRegistrationView(generics.CreateAPIView):
    serializer_class = SellerRegistrationSerializer


# SELLER LOGIN
class LoginView(generics.GenericAPIView):
    serializer_class = SellerLoginSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        seller = authenticate(username=username, password=password)

        if seller:
            refresh = RefreshToken.for_user(seller)
            seller_serializer = SellerSerializer(seller)
            return Response({
                'refresh': str(refresh),
                'access token': str(refresh.access_token),
                'seller': seller_serializer.data['username']
            })
        else:
            return Response({'detail': 'Invalid Credentials !'})


class SellerDashboardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        seller = request.user
        serializer = SellerSerializer(seller)
        return Response({
            'message': "Welcome to dashboard.",
            'Information': serializer.data
        })
