from rest_framework.viewsets import ModelViewSet

from rebalancer.api.serializers import AccountPositionSerializer
from rebalancer.models import AccountPosition


class AccountPositionViewSet(ModelViewSet):
    queryset = AccountPosition.objects.all()
    serializer_class = AccountPositionSerializer
