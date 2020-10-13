from rest_framework import viewsets
from rest_framework import permissions

from .models import Restauraunt
from .serializers import RestaurauntSerializer


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

