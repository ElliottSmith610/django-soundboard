from rest_framework.serializers import ModelSerializer
from base.models import SoundClip

class SoundClipSerializer(ModelSerializer):
    class Meta:
        model = SoundClip
        fields = '__all__'