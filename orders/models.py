from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from articles.models import Article

IN_PROGRESS = 0
CANCELED = 1
CONFIRMED = 2
FINISHED = 3

ORDER_STATUS_CHOICES = [
    (IN_PROGRESS, 'In progress'),
    (CANCELED, 'Canceled'),
    (CONFIRMED, 'Confirmed'),
    (FINISHED, 'Finished')
]


class OrderArticle(models.Model):
    quantity = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self):
        if self.quantity < 1:
            raise ValidationError("Quantity can't be lower then 1.")

    @property
    def subtotal(self):
        return self.quantity * self.article.price


class Order(models.Model):
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', db_index=True)
    articles = models.ManyToManyField(OrderArticle, related_name='order')

    @property
    def subtotal(self):
        return sum(article.subtotal for article in self.articles.all())
