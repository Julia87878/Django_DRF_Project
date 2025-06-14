from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="Пользователь",
    )
    payment_date = models.DateField(
        verbose_name="Дата оплаты", help_text="Укажите дату оплаты."
    )
    paid_course = models.CharField(
        max_length=250,
        verbose_name="Оплаченный курс",
        help_text="Укажите оплаченный курс.",
        blank=True,
        null=True,
    )
    paid_lesson = models.CharField(
        max_length=250,
        verbose_name="Оплаченный урок",
        help_text="Укажите оплаченный урок.",
        blank=True,
        null=True,
    )
    payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма оплаты",
        help_text="Укажите сумму оплаты.",
    )
    payment_method = models.CharField(
        max_length=30,
        verbose_name="Способ оплаты",
        help_text="Укажите способ оплаты.",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "платёж"
        verbose_name_plural = "платежи"
        ordering = [
            "user",
            "payment_date",
            "paid_course",
            "paid_lesson",
            "payment_amount",
            "payment_method",
        ]

    def __str__(self):
        return f"{self.user} {self.payment_date} {self.paid_course} {self.paid_lesson} {self.payment_amount}."
