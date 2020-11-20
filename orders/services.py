from django.contrib.auth.models import User

from articles.models import Article
from articles.selectors import get_article_by_pk
from orders.models import Order, OrderArticle
from orders.selectors import get_order_by_pk, get_order_article_by_order_and_article_pk


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


def order_add_article(*, pk_order: int, article: dict):
    order = get_order_by_pk(pk_order=pk_order)
    if order.articles.filter(article_id=article['pk']).exists():
        return order_update_order_article(pk_order=pk_order, article=article)
    db_article = get_article_by_pk(pk_article=article['pk'])
    order_article = order_article_create(article=db_article, quantity=article['quantity'])
    order.articles.add(order_article)
    order.save()
    return order


def order_update_order_article(*, pk_order: int, article: dict) -> OrderArticle:
    order_article = get_order_article_by_order_and_article_pk(pk_order=pk_order, pk_article=article['pk'])
    order_article.quantity = article['quantity']
    order_article.save()
    return order_article


def order_update_status_by_user(*, pk_order: int, status: int) -> Order:
    order = get_order_by_pk(pk_order=pk_order)
    order.status = status
    order.save()
    return order
