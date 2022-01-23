from django.urls import path, include
from rest_framework import routers
from app_production import views

router = routers.DefaultRouter()
router.register(r'extended', views.FullViewSet, basename='Extended procucts')
router.register(r'products', views.OnlyProductViewSet, basename='Products')
router.register(r'processs', views.OnlyProcessViewSet, basename='Processs')
router.register(r'data', views.ProcesDataViewSet, basename='Process data')
router.register(r'images', views.ImageViewSet, basename='Images')

app_name = "app_production" # do wyłuskania {% url %}

urlpatterns = [
    path('api/', include(router.urls)),
    path('list/', views.product_list_view, name='list'),
    path('detail/<int:pk>/', views.product_detail_view, name='detail'),
    path('image/list/', views.image_list_view, name='images'),
]


