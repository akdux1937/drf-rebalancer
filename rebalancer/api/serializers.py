from rest_framework import serializers

from rebalancer.models import AccountPosition


class AccountPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountPosition
        fields = ["id", "ticker", "shares"]
        read_only_fields = ("id",)
