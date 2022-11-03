from rest_framework import viewsets
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializers, SongSerializers, LyricSerializers


# Create your views here.
class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializers
   
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers
   
class LyricViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializers
