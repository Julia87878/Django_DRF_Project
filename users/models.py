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
        blank=True,
        null=True,
    )
    payment_date = models.DateField(auto_now_add=True, verbose_name="Дата оплаты")
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
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма оплаты",
        help_text="Укажите сумму оплаты.",
        blank=True,
        null=True,
    )
    payment_method = models.CharField(
        max_length=30,
        verbose_name="Способ оплаты",
        help_text="Укажите способ оплаты.",
        blank=True,
        null=True,
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name="Id сессии",
        help_text="Укажите id ceccии.",
        blank=True,
        null=True,
    )
    link = models.URLField(
        max_length=400,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату.",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
        ordering = [
            "user",
            "payment_date",
            "paid_course",
            "paid_lesson",
            "amount",
            "payment_method",
        ]

    def __str__(self):
        return f"{self.user} {self.payment_date} {self.paid_course} {self.paid_lesson} {self.amount}."
