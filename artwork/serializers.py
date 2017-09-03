from rest_framework import serializers
from artwork.models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ('id', 'author', 'type', 'category', 'miniature', 'description', 'attachment', 'title')
        depth = 1
