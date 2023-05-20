import uuid

from django.db import models


class AccountPosition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ticker = models.CharField(max_length=25)
    shares = models.DecimalField(max_digits=13, decimal_places=4)

    def __str__(self):
        return f"{self.ticker}"
