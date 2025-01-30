from django.contrib import admin
from django.urls import path, include
from product_catalog import urls as product_urls
from product_catalog.views import SellerRegistrationView, LoginView, SellerDashboardView  # SellerLoginView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny


class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]  # Override default permission to allow anyone to get token


class RefreshTokenView(TokenRefreshView):
    permission_classes = [AllowAny]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('product/', include(product_urls)),
    path('/signup', SellerRegistrationView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('dashboard', SellerDashboardView.as_view(), name='dashboard'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
