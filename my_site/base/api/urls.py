from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('clips', views.getClips),
    path('clips/<int:pk>', views.getClip),
]