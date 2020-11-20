from rest_framework import permissions, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from usereats.utils import inline_serializer
from .models import Order
from .services import order_create, order_add_article, order_update_order_article, order_update_status_by_user
from .selectors import get_in_progress_order, get_user_order_list


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class OrderListApi(APIView):
    """
    Lists orders for authenticated user.
    """
    permission_classes = [permissions.IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        articles = inline_serializer(many=True, fields={
            'article': inline_serializer(fields={
                'pk': serializers.IntegerField(),
                'name': serializers.CharField(),
            }),
            'quantity': serializers.IntegerField(),
        })

        class Meta:
            model = Order
            fields = ('pk', 'status', 'articles', 'subtotal')

    def get(self, request):
        orders = get_user_order_list(user=request.user)
        serializer = self.OutputSerializer(orders, many=True)
        return Response(data=serializer.data)


class OrderCreateApi(APIView):
    """
    Creates new order with one article.
    One article is required to create an order.
    """
    permission_classes = [permissions.IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        article = inline_serializer(fields={
            'pk': serializers.IntegerField(),
            'quantity': serializers.IntegerField(),
        })

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_create(user=request.user, **serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class OrderInProgressApi(APIView):
    """
    Get any order that is currently in-progress.
    """
    permission_classes = [permissions.IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        articles = inline_serializer(many=True, fields={
            'article': inline_serializer(fields={
                    'pk': serializers.IntegerField(),
                    'name': serializers.CharField()
                }),
            'quantity': serializers.IntegerField(),
        })

        class Meta:
            model = Order
            fields = ('pk', 'status', 'articles', 'subtotal')

    def get(self, request):
        order = get_in_progress_order(user=request.user)
        serializer = self.OutputSerializer(order)
        return Response(data=serializer.data)


class OrderAddOrderArticleApi(APIView):
    """
    Add new article to order.
    """
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    class InputSerializer(serializers.Serializer):
        article = inline_serializer(fields={
            'pk': serializers.IntegerField(),
            'quantity': serializers.IntegerField(),
        })

    def post(self, request, pk_order):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_add_article(pk_order=pk_order, **serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class OrderUpdateOrderArticleApi(APIView):
    """
    Update order article in order.
    """
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    class InputSerializer(serializers.Serializer):
        article = inline_serializer(fields={
            'pk': serializers.IntegerField(),
            'quantity': serializers.IntegerField(),
        })

    def post(self, request, pk_order):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_update_order_article(pk_order=pk_order, **serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class OrderCancelApi(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def post(self, request, pk_order):
        order_update_status_by_user(pk_order=pk_order, status=1)
        return Response(status=status.HTTP_200_OK)


class OrderConfirmApi(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def post(self, request, pk_order):
        order_update_status_by_user(pk_order=pk_order, status=2)
        return Response(status=status.HTTP_200_OK)
