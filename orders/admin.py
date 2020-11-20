from django.contrib import admin

# Register your models here.
from orders.models import Order, OrderArticle

admin.site.register(Order)
admin.site.register(OrderArticle)
