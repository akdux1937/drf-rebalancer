import uuid

from django.db import models


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    taxable = models.BooleanField()

    def __str__(self):
        return self.name


class AccountPosition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ticker = models.CharField(max_length=25)
    shares = models.DecimalField(max_digits=13, decimal_places=4)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account_positions")

    def __str__(self):
        return f"{self.account.name}:{self.ticker} ({self.shares})"
