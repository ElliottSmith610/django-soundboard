from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Message, SoundClip, User

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # 'name', 

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


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
        fields = ['username', 'email', 'name', 'avatar', 'bio']
