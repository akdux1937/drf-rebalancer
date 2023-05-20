from rest_framework import generics

from rebalancer.api.serializers import AccountSerializer, AccountPositionSerializer
from rebalancer.models import Account, AccountPosition


class ListAddAccount(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AddAccountPosition(generics.CreateAPIView):
    queryset = AccountPosition.objects.all()
    serializer_class = AccountPositionSerializer


class AccountPositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountPosition.objects.all()
    serializer_class = AccountPositionSerializer
    lookup_url_kwarg = "position_pk"
