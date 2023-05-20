from django.urls import path

from rebalancer.api.views import ListAddAccount, AccountDetail, AccountPositionDetail, AddAccountPosition


urlpatterns = [
    path("api/accounts", ListAddAccount.as_view(), name="all-accounts"),
    path("api/accounts/<uuid:pk>/", AccountDetail.as_view(), name="account-detail"),
    path("api/accounts/<uuid:pk>/account-positions/",
         AddAccountPosition.as_view(), name="add-account-position"),
    path("api/accounts/<uuid:pk>/account-positions/<uuid:position_pk>/",
         AccountPositionDetail.as_view(), name="account-position-detail"),
]
