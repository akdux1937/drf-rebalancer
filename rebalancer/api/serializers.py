from rest_framework import serializers

from rebalancer.models import AccountPosition, Account


class AccountPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountPosition
        fields = ["id", "ticker", "shares"]
        read_only_fields = ("id",)

    def create(self, validated_data, **kwargs):
        validated_data['account_id'] = self.context['request'].parser_context['kwargs']['pk']
        return super(AccountPositionSerializer, self).create(validated_data)


class AccountSerializer(serializers.ModelSerializer):
    account_positions = AccountPositionSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ["id", "name", "taxable", "account_positions"]
