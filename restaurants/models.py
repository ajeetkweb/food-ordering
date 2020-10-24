from django.db import models

from django.utils.text import slugify
from django.contrib.auth.models import User


def upload_logo(instance, filename):
    return f'images/logo/{instance.pk}' \
           f'/{slugify(instance.name)}-logo.{filename.split(".")[-1]}'


# Create your models here.
class Restauraunt(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(null=True, upload_to=upload_logo)

    def __str__(self) -> str:
        return self.name