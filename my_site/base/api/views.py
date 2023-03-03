from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import SoundClip
from .serializers import SoundClipSerializer

@api_view(['GET'])   # Specify methods ('GET', 'PUT', 'POST', 'PATCH', 'DELETE')
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/clips',
        'GET /api/clips/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getClips(request):
    clips = SoundClip.objects.all()
    # list_clips = {clip.id: [clip.title, clip.description, clip.person.name] for clip in clips}
    serializer = SoundClipSerializer(clips, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getClip(request, pk):
    clip = SoundClip.objects.get(id=pk)
    # list_clips = {clip.id: [clip.title, clip.description, clip.person.name] for clip in clips}
    serializer = SoundClipSerializer(clip, many=False)
    return Response(serializer.data) 