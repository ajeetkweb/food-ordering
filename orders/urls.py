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
    path('', OrderListApi.as_view(), name='list-orders-api'),
    path('create/', OrderCreateApi.as_view(), name='create-order-api'),
    path('cancel/<int:pk_order>', OrderCancelApi.as_view(), name='cancel-order-api'),
    path('confirm/<int:pk_order>', OrderConfirmApi.as_view(), name='confirm-order-api'),
    path('in-progress/', OrderInProgressApi.as_view(), name='order-in-progress-api'),
    path('add-article/<int:pk_order>', OrderAddOrderArticleApi.as_view(), name='add-order-article-api'),
    path('update-article/<int:pk_order>', OrderUpdateOrderArticleApi.as_view(), name='update-order-article-api'),
]