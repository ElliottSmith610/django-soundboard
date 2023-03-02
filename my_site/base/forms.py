from django.forms import ModelForm
from .models import Message, SoundClip

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__' #['body']

class SoundclipForm(ModelForm):
    class Meta:
        model = SoundClip
        fields = '__all__'
        exclude = ['commenters', 'location']
