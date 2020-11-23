import factory
from django.contrib.auth.models import User

from orders.models import IN_PROGRESS, OrderArticle

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)


class RestaurantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'restaurants.Restauraunt'

    owner = factory.SubFactory(UserFactory)


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'articles.Article'

    price = 10.0
    owner = factory.SubFactory(RestaurantFactory)


class OrderArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.OrderArticle'

    quantity = 1
    article = factory.SubFactory(ArticleFactory)


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    articles = factory.SubFactory(OrderArticleFactory)
    user = factory.SubFactory(UserFactory)
    status = IN_PROGRESS
    
    @factory.post_generation
    def articles(self, create, extracted, **kwargs):
        if not create:
            self.articles.add(OrderFactory(user=self.user))
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for article in extracted:
                self.articles.add(article)
