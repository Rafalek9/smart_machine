from django.urls import path, include
from rest_framework import routers
from app_maintenance import views


router = routers.DefaultRouter()
router.register(r'fault', views.FaultViewSet, basename='faults')
router.register(r'status', views.StatusViewSet, basename='statuss')


app_name = "app_maintenance"
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/fault/clear/code=<int:code>/', views.clear_selected_faults, ),
    path('api/fault/clear/st=<int:station_number>/', views.clear_station_faults, ),
    path('api/fault/clear/all/', views.clear_all_faults, ),
]
