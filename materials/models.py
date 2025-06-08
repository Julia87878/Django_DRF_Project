from django.db import models


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
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Превью (картинка)",
        help_text="Загрузите превью (картинку) курса.",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
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
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ["name", "course"]

    def __str__(self):
        return f"{self.name} {self.course}."
