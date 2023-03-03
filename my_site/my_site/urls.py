from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('base.urls')),

    path('api/', include('base.api.urls')),
    #path('api-auth/', include('rest_framework.urls')),
]
