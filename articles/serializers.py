from rest_framework import serializers

from .models import Article
from restaurants.models import Restauraunt


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    id_restaurant = serializers.PrimaryKeyRelatedField(queryset=Restauraunt.objects.all(), source="owner.id")
    class Meta:
        model = Article
        fields = ['pk', 'name', 'description', 'price', 'id_restaurant']
