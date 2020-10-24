from django.db import models

from restaurants.models import Restauraunt


class Article(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    owner = models.ForeignKey(Restauraunt, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.name