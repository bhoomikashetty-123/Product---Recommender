from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.api import ProductViewSet
from orders.api import OrderViewSet
from products.views import recommend_products
from orders.views import create_order

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns =  [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/recommend/', recommend_products),
    path('api/create-order/', create_order),
    path('dashboard/', include('dashboard.urls')),
]


