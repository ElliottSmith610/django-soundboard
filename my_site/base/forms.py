from django.forms import ModelForm
from .models import Message, SoundClip
from django.contrib.auth.models import User

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__' #['body']

class SoundclipForm(ModelForm):
    class Meta:
        model = SoundClip
        fields = '__all__'
        exclude = ['commenters', 'location']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
