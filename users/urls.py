from django.urls import path

from users.apps import UsersConfig

from .views import (
    CustomUserCreateAPIView,
    PaymentCreateAPIView,
    PaymentDestroyAPIView,
    PaymentListAPIView,
    PaymentRetrieveAPIView,
    PaymentUpdateAPIView,
)

app_name = UsersConfig.name


urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payments_list"),
    path(
        "payments/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment_retrieve"
    ),
    path("payments/new/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path(
        "payments/update/<int:pk>/",
        PaymentUpdateAPIView.as_view(),
        name="payment_update",
    ),
    path(
        "payments/delete/<int:pk>/",
        PaymentDestroyAPIView.as_view(),
        name="payment_delete",
    ),
    path("users/new/", CustomUserCreateAPIView.as_view(), name="customuser_create"),
]
