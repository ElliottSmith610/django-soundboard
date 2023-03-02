from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('profile/<int:pk>', views.userProfile, name='user-profile'),
    path('update-user/', views.updateUser, name="update-user"),

    path('soundboard/', views.soundboard, name="soundboard"),
    path('soundboard/<int:pk>/', views.individual_clip, name="individual_clip"),
    path('soundboard/<int:pk>/edit/', views.editClip, name="edit-clip"),
    path('soundboard/<int:pk>/delete-clip/', views.deleteClip, name="delete-clip"),
    path('soundboard/delete-comment/<int:pk>', views.deleteComment, name="delete-comment"),
    path('soundboard/upload', views.uploadClip, name='upload-clip'),

    path('soundboard/clips/', views.clipsPage, name="clips"),
    path('soundboard/activities/', views.activitiesPage, name="activities"),

    path('test/', views.test, name='test'),
]