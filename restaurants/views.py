from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Restauraunt
from .serializers import RestaurauntSerializer, RestaurantDetailsSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API viewset to read all Restaurants.
    """
    queryset = Restauraunt.objects.all()
    serializer_class = RestaurauntSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RestaurantDetailsSerializer(instance)
        return Response(serializer.data)
