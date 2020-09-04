from maas.models.movie import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'year', 'rank', 'rating')
