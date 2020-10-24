from rest_framework import serializers

from .models import Restauraunt
from articles.serializers import ArticleSerializer


class RestaurauntSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restauraunt
        fields = ['pk', 'name', 'logo']


class RestaurantDetailsSerializer(serializers.HyperlinkedModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Restauraunt
        fields = ['pk', 'name', 'logo', 'articles']