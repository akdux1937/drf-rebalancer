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
    account_positions = AccountPositionSerializer(many=True)

    class Meta:
        model = Account
        fields = ["id", "name", "taxable", "account_positions"]

    def create(self, validated_data):
        positions_data = validated_data.pop('account_positions')
        account = Account.objects.create(**validated_data)

        for position_data in positions_data:
            AccountPosition.objects.create(account=account, **position_data)

        return account
