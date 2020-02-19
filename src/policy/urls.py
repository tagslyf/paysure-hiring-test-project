from django.conf.urls import url, include
from rest_framework import routers

from .views import PaymentViewSet, PolicyViewSet


policy_router = routers.DefaultRouter()
policy_router.register('', PolicyViewSet)

payment_router = routers.DefaultRouter()
payment_router.register('', PaymentViewSet)

urlpatterns = [
    url(r'^policy/', include(policy_router.urls)),
    url(r'^payment/', include(payment_router.urls)),
]
