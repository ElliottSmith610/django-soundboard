from django.contrib import admin

# Register your models here.
from .models import SoundClip, Person, Message, User

admin.site.register(User)
admin.site.register(Person)
admin.site.register(SoundClip)
admin.site.register(Message)
