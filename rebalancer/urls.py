from django.urls import path, include
from rest_framework import routers

from rebalancer.api.viewsets import AccountPositionViewSet


router = routers.DefaultRouter()
router.register("account-positions", AccountPositionViewSet, basename="account-positions")

urlpatterns = [
    path("api/", include(router.urls)),
]
