from typing import Optional, List

from django.contrib.auth.models import User

from orders.models import Order, OrderArticle


def get_in_progress_order(*, user: User) -> Optional[Order]:
    return Order \
        .objects \
        .filter(user=user, status=0) \
        .first()


def get_order_by_pk(*, pk_order: int) -> Order:
    return Order \
        .objects \
        .get(pk=pk_order)


def get_order_article_by_order_and_article_pk(*, pk_order: int, pk_article: int) -> OrderArticle:
    return OrderArticle \
        .objects \
        .filter(order__pk=pk_order, article__pk=pk_article) \
        .first()


def get_user_order_list(*, user: User) -> List[Order]:
    return Order \
        .objects \
        .prefetch_related('articles') \
        .filter(user=user) \
        .all()
