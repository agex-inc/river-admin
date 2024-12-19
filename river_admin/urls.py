from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from river_admin.views import urls

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
] + urls
