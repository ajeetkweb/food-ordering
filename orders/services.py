from typing import Optional
from django.contrib.auth.models import User

from articles.models import Article
from articles.selectors import get_article_by_pk
from orders.models import Order, OrderArticle
from orders.selectors import get_order_article_by_order_and_article_pk_for_user, get_order_by_pk_for_user


def order_create(*, user: User, article: dict) -> Order:
    db_article = get_article_by_pk(pk_article=article['pk'])
    order_article = order_article_create(article=db_article, quantity=article['quantity'])
    order = Order.objects.create(user=user, status=0)
    order.articles.set([order_article])
    order.save()
    return order


def order_article_create(*, article: Article, quantity: int) -> OrderArticle:
    order_article = OrderArticle.objects.create(article=article, quantity=quantity)
    order_article.save()
    return order_article


def order_add_article(*, pk_order: int, user: User, article: dict):
    try:
        order = get_order_by_pk_for_user(pk_order=pk_order, user=user)
        if order.articles.filter(article_id=article['pk']).exists():
            return order_update_order_article(pk_order=pk_order, user=user, article=article)
        db_article = get_article_by_pk(pk_article=article['pk'])
        order_article = order_article_create(article=db_article, quantity=article['quantity'])
        order.articles.add(order_article)
        order.save()
    except (Order.DoesNotExist, Article.DoesNotExist):
        order = None
    finally:
        return order


def order_update_order_article(*, pk_order: int, user: User, article: dict) -> Optional[OrderArticle]:
    try:
        order_article = get_order_article_by_order_and_article_pk_for_user(pk_order=pk_order, pk_article=article['pk'], user=user)
        order_article.quantity = article['quantity']
        order_article.save()
    except OrderArticle.DoesNotExist:
        order_article = None
    finally:
        return order_article


def order_update_status_by_user(*, pk_order: int, user: User, status: int) -> Optional[Order]:
    try:
        order = get_order_by_pk_for_user(pk_order=pk_order, user=user)
        order.status = status
        order.save()
    except Order.DoesNotExist:
        order = None
    finally:
        return order
