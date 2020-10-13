from rest_framework import serializers

from .models import Restauraunt


class RestaurauntSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restauraunt
        fields = ['id', 'name', 'logo']