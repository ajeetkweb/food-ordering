from rest_framework import status
from rest_framework.test import APITestCase

from usereats import mock_factories

from orders.models import CONFIRMED, IN_PROGRESS, CANCELED


class TestOrdersAPI(APITestCase):

    def setUp(self):
        self.user = mock_factories.UserFactory.create()

    def login_user(self):
        self.client.force_authenticate(user=self.user)

    def logout_user(self):
        self.client.logout()

    def test_create_order_unauthenticated(self):
        article = mock_factories.ArticleFactory.create()
        payload = {
            "article": {
                "pk": article.pk,
                "quantity": 1
            }
        }
        response = self.client.post(
            "/api/orders/create/", data=payload, format="json")
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_new_order_no_previous_order(self):
        article = mock_factories.ArticleFactory.create()
        self.login_user()
        payload = {
            "article": {
                "pk": article.pk,
                "quantity": 1
            }
        }
        response = self.client.post(
            "/api/orders/create/", data=payload, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.logout_user()

    def test_create_new_order_but_previous_order(self):
        article = mock_factories.ArticleFactory.create()
        _order = mock_factories.OrderFactory(user=self.user)
        self.login_user()
        payload = {
            "article": {
                "pk": article.pk,
                "quantity": 1
            }
        }
        response = self.client.post(
            "/api/orders/create/", data=payload, format="json")
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.logout_user()

    def test_get_order_in_progress_unauthenticated(self):
        response = self.client.get("/api/orders/in-progress/")
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_order_in_progress_order_not_exist(self):
        self.login_user()
        response = self.client.get("/api/orders/in-progress/")
        response_json = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_json["status"], None)
        self.logout_user()

    def test_get_order_in_progress_order_exists(self):
        order = mock_factories.OrderFactory(user=self.user)
        self.login_user()
        response = self.client.get("/api/orders/in-progress/")
        response_json = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_json["pk"], order.pk)
        self.assertEquals(response_json["status"], IN_PROGRESS)
        self.logout_user()

    def test_order_cancel_not_authenticated(self):
        response = self.client.get("/api/orders/cancel/1")
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_order_cancel_order_not_exists(self):
        self.login_user()
        response = self.client.post("/api/orders/cancel/1")
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.logout_user()

    def test_order_cancel_order_order_exists(self):
        order = mock_factories.OrderFactory(user=self.user)
        self.login_user()
        response = self.client.post(f"/api/orders/cancel/{order.pk}")
        order.refresh_from_db()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(order.status, CANCELED)
        self.logout_user()

    def test_cancel_order_not_owned_by_user(self):
        other_users_order = mock_factories.OrderFactory.create()
        self.login_user()
        response = self.client.post(
            f"/api/orders/cancel/{other_users_order.pk}")
        other_users_order.refresh_from_db()
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(other_users_order.status, IN_PROGRESS)
        self.logout_user()

    def test_order_confirm_not_authenticated(self):
        response = self.client.get("/api/orders/confirm/1")
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_order_confirm_order_not_exists(self):
        self.login_user()
        response = self.client.post("/api/orders/confirm/1")
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.logout_user()

    def test_order_confirm_order_order_exists(self):
        order = mock_factories.OrderFactory(user=self.user)
        self.login_user()
        response = self.client.post(f"/api/orders/confirm/{order.pk}")
        order.refresh_from_db()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(order.status, CONFIRMED)
        self.logout_user()

    def test_confirm_order_not_owned_by_user(self):
        other_users_order = mock_factories.OrderFactory.create()
        self.login_user()
        response = self.client.post(
            f"/api/orders/confirm/{other_users_order.pk}")
        other_users_order.refresh_from_db()
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(other_users_order.status, IN_PROGRESS)
        self.logout_user()

    def test_add_article_to_order_not_authenticated(self):
        order = mock_factories.OrderFactory(user=self.user)
        article = mock_factories.ArticleFactory.create()
        payload = {
            'article': {
                'pk': article.pk,
                'quantity': 1
            }
        }
        response = self.client.post(
            f"/api/orders/add-article/{order.pk}", data=payload, format='json')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_article_to_existing_order(self):
        order = mock_factories.OrderFactory(user=self.user)
        old_subtotal = order.subtotal
        self.login_user()
        article = mock_factories.ArticleFactory.create()
        payload = {
            'article': {
                'pk': article.pk,
                'quantity': 1
            }
        }
        response = self.client.post(
            f"/api/orders/add-article/{order.pk}", data=payload, format='json')
        order.refresh_from_db()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(order.subtotal, old_subtotal + article.price)
        self.logout_user()

    def test_add_article_to_existing_canceled_order(self):
        order = mock_factories.OrderFactory(user=self.user, status=CANCELED)
        self.login_user()
        article = mock_factories.ArticleFactory.create()
        payload = {
            'article': {
                'pk': article.pk,
                'quantity': 1
            }
        }
        response = self.client.post(
            f"/api/orders/add-article/{order.pk}", data=payload, format='json')
        order.refresh_from_db()
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.logout_user()

    def test_add_article_to_other_users_order(self):
        other_user = mock_factories.UserFactory.create()
        other_users_order = mock_factories.OrderFactory(user=other_user, status=CANCELED)
        self.login_user()
        article = mock_factories.ArticleFactory.create()
        payload = {
            'article': {
                'pk': article.pk,
                'quantity': 1
            }
        }
        response = self.client.post(
            f"/api/orders/add-article/{other_users_order.pk}", data=payload, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.logout_user()


    def test_add_article_to_not_existing_order(self):
        self.login_user()
        article = mock_factories.ArticleFactory.create()
        payload = {
            'article': {
                'pk': article.pk,
                'quantity': 1
            }
        }
        response = self.client.post(
            f"/api/orders/add-article/13371", data=payload, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.logout_user()

    def test_update_article_not_authenticated(self):
        order_article = mock_factories.OrderArticleFactory.create()
        order = mock_factories.OrderFactory(
            user=self.user, articles=[order_article])
        article = order_article.article
        payload = {
            'article': {
                'pk': article.pk,
                'quantity': order_article.quantity + 1
            }
        }
        response = self.client.post(
            f"/api/orders/update-article/{order.pk}", data=payload, format='json')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_article_on_not_existing_order(self):
        self.login_user()
        order_article = mock_factories.OrderArticleFactory.create()
        article = order_article.article
        payload = {
            'article': {
                'pk': article.pk,
                'quantity': order_article.quantity + 1
            }
        }
        response = self.client.post(
            f"/api/orders/update-article/131231", data=payload, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.logout_user()

    def test_update_article_on_existing_order(self):
        self.login_user()
        order_article = mock_factories.OrderArticleFactory.create()
        order = mock_factories.OrderFactory(
            user=self.user, articles=[order_article])
        article = order_article.article
        payload = {
            'article': {
                'pk': article.pk,
                'quantity': order_article.quantity + 1
            }
        }
        response = self.client.post(
            f"/api/orders/update-article/{order.pk}", data=payload, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.logout_user()

    def test_update_article_on_other_users_order(self):
        self.login_user()
        other_user = mock_factories.UserFactory.create()
        order_article = mock_factories.OrderArticleFactory.create()
        other_users_order = mock_factories.OrderFactory(
            user=other_user, articles=[order_article])
        article = order_article.article
        payload = {
            'article': {
                'pk': article.pk,
                'quantity': order_article.quantity + 1
            }
        }
        response = self.client.post(
            f"/api/orders/update-article/{other_users_order.pk}", data=payload, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.logout_user()

    def test_update_article_on_existing_canceled_order(self):
        self.login_user()
        order_article = mock_factories.OrderArticleFactory.create()
        order = mock_factories.OrderFactory(
            user=self.user, articles=[order_article], status=CANCELED)
        article = order_article.article
        payload = {
            'article': {
                'pk': article.pk,
                'quantity': order_article.quantity + 1
            }
        }
        response = self.client.post(
            f"/api/orders/update-article/{order.pk}", data=payload, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.logout_user()
