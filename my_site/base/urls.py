from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('soundboard/', views.soundboard, name="soundboard"),
    path('soundboard/<int:pk>/', views.individual_clip, name="individual_clip"),
    path('soundboard/<int:pk>/edit/', views.editClip, name="edit"),
    path('soundboard/<int:pk>/delete/', views.deleteClip, name="delete"),
    path('soundboard/upload', views.uploadClip, name='upload-clip'),
    path('test/', views.test, name='test'),
]