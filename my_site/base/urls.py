from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('soundboard/', views.soundboard, name="soundboard"),
    path('soundboard/<int:pk>', views.individual_clip, name="individual_clip"),
    # path('soundboard/upload', views.upload, name='upload')
    path('test/', views.test, name='test'),
]