from django.urls import path

from orders.apis import (
    OrderListApi,
    OrderCancelApi,
    OrderConfirmApi,
    OrderCreateApi,
    OrderInProgressApi,
    OrderAddOrderArticleApi,
    OrderUpdateOrderArticleApi,
)

order_patterns = [
    path('', OrderListApi.as_view(), name='list-orders'),
    path('create/', OrderCreateApi.as_view(), name='create-order'),
    path('cancel/<int:pk_order>', OrderCancelApi.as_view(), name='cancel-order'),
    path('confirm/<int:pk_order>', OrderConfirmApi.as_view(), name='confirm-order'),
    path('in-progress/', OrderInProgressApi.as_view(), name='order-in-progress'),
    path('add-order-article/<int:pk_order>', OrderAddOrderArticleApi.as_view(), name='add-order-article'),
    path('update-order-article/<int:pk_order>', OrderUpdateOrderArticleApi.as_view(), name='update-order-article'),
]