from django.urls import path, re_path, include
from django.contrib import admin
from demo.view import approve_issue, approve_shipping

urlpatterns = [
    re_path(r'^approve_issue/(?P<issue_id>\d+)/(?P<next_state_id>\d+)/$', approve_issue, name='approve_issue'),
    re_path(r'^approve_shipping/(?P<shipping_id>\d+)/(?P<next_state_id>\d+)/$', approve_shipping, name='approve_shipping'),
    path('admin/', admin.site.urls),
    path('', include("river_admin.urls")),
    path('api-auth/', include('rest_framework.urls')),
]
