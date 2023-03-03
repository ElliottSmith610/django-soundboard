from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    

class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class SoundClip(models.Model):
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=300)
    # file = models.FileField
    commenters = models.ManyToManyField(User, related_name='commenters', blank=True) ###
    # If User was already being used by another key, eg person
    # commenters = models.ManyToManyField(User, related_name='commenters', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Returns the most recently updated/created items
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    soundclip = models.ForeignKey(SoundClip, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Returns the most recently updated/created items
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
    
    
