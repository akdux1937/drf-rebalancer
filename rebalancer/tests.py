import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from rebalancer.models import Account, AccountPosition


@pytest.mark.django_db
def test_valid_account_is_created():
    url = reverse("all-accounts")
    data = {
        "name": "ATK",
        "taxable": False,
    }
    client = APIClient()
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Account.objects.get().name == "ATK"


@pytest.mark.django_db
def test_account_name_missing_returns_bad_request():
    url = reverse("all-accounts")
    data = {
        "something_else": "blahblah",
        "taxable": False,
    }
    client = APIClient()
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
