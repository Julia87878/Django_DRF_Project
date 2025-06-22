from django.db import models

from users.models import CustomUser


class Course(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Название",
        help_text="Введите название курса.",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание курса.",
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Укажите цену курса.",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="Владелец",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Превью (картинка)",
        help_text="Загрузите превью (картинку) курса.",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Название",
        help_text="Введите название урока.",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Укажите описание урока",
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Укажите цену урока.",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Владелец",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Курс",
    )

    image = models.ImageField(
        upload_to="images/",
        verbose_name="Превью(картинка)",
        help_text="Загрузите превью(картинку) урока.",
        blank=True,
        null=True,
    )
    video_url = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео.",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name", "course"]

    def __str__(self):
        return f"{self.name} {self.course}."


class Subscription(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="subscriptions",
        verbose_name="Пользователь",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subscriptions",
        verbose_name="Курс",
    )
    is_active_subscription = models.BooleanField(
        default=True, verbose_name="Признак подписки"
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ["user", "course"]

    def __str__(self):
        return f"{self.user} {self.course}."
