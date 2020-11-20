from rest_framework import serializers

from articles.serializers import ArticleSerializer
from .models import Order, OrderArticle


class OrderArticlesSerializer(serializers.HyperlinkedModelSerializer):
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = OrderArticle
        fields = ['article', 'quantity']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Order
        fields = ['pk', 'status', 'articles']
