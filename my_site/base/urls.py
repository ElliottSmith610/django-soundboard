from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('soundboard/', views.soundboard, name="soundboard"),
    path('test/', views.test, name='test')
]