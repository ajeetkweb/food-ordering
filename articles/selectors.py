from articles.models import Article


def get_article_by_pk(*, pk_article: int) -> Article:
    return Article.objects.get(pk=pk_article)
