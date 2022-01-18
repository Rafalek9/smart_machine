from django.urls import path, include
from rest_framework import routers
from app_production import views

router = routers.DefaultRouter()
router.register(r'full_product', views.FullViewSet, basename='Full product')
router.register(r'only_product', views.OnlyProductViewSet, basename='Only product')
router.register(r'only_process', views.OnlyProcessViewSet, basename='Only process')
router.register(r'images', views.ImageViewSet, basename='Images')

app_name = "app_production" # do wyłuskania {% url %}

urlpatterns = [
    path('api/', include(router.urls)),
    path('list/', views.product_list_view, name='list'),
    path('detail/<int:pk>/', views.product_detail_view, name='detail'),
    path('image/list/', views.image_list_view, name='images'),
]
