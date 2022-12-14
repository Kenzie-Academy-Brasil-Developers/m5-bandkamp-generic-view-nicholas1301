from rest_framework import serializers

from .models import Song
from albums.models import Album
from albums.serializers import AlbumSerializer


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]
