from django.urls import path
from . import views

urlpatterns = [
        path('', views.product_overview),
        path('list/', views.product_list),
        path('<int:pk>', views.product_detail),
        path('create/', views.CreateProductView.as_view(), name='create'),
        path('update/<int:pk>', views.UpdateProducView.as_view(), name='update'),
        path('delete/<int:pk>', views.delete_product),
        path('seller/<int:pk>', views.seller_product),
]