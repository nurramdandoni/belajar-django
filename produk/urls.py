from django.urls import path
from . import views

urlpatterns = [
    path('api/produk', views.dataProducts, name='dataProducts'),
    path('api/produk/<int:id>', views.dataProductsDetail, name='dataProductsDetail'),
]