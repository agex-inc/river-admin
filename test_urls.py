from django.urls import path, re_path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("river_admin.urls")),
    path('api-auth/', include('rest_framework.urls')),
]
