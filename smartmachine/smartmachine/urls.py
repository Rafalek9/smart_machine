from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import dashboard_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # sites
    path('', dashboard_view),

    # included apps
    path('machine/', include('app_machine.urls')),
    path('production/', include('app_production.urls')),
    path('maintenance/', include('app_maintenance.urls')),
    path('reference/', include('app_reference.urls')),

    # predefined view
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Enbotic Smart Machine'
admin.site.index_title = 'Traceability'
admin.site.site_title = 'Smart Machine'
