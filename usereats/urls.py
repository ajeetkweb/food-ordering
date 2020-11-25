"""usereats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from restaurants import apis as restaurant_api
from articles import apis as articles_api

from orders.urls import order_patterns
from rest_framework import status
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView


class HealthCheckApi(GenericAPIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)


router = routers.DefaultRouter()
router.register('restaurants', restaurant_api.RestaurantApi)
router.register('articles', articles_api.ArticlesApi)


urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/health/', HealthCheckApi.as_view(), name='health-api'),
    path('api/orders/', include((order_patterns, 'orders'))),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
