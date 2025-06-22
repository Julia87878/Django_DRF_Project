from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

from .views import (
    CustomUserCreateAPIView,
    CustomUserDestroyAPIView,
    CustomUserListAPIView,
    CustomUserRetrieveAPIView,
    CustomUserUpdateAPIView,
    PaymentCreateApiView,
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
    path("payments/new/", PaymentCreateApiView.as_view(), name="payment_create"),
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
    path("register/", CustomUserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("", CustomUserListAPIView.as_view(), name="customusers_list"),
    path("<int:pk>/", CustomUserRetrieveAPIView.as_view(), name="customuser_retrieve"),
    path(
        "update/<int:pk>/",
        CustomUserUpdateAPIView.as_view(),
        name="customuser_update",
    ),
    path(
        "delete/<int:pk>/",
        CustomUserDestroyAPIView.as_view(),
        name="customuser_delete",
    ),
]
