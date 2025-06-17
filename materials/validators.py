import re

from rest_framework.serializers import ValidationError


class UrlCustomValidator:
    """Проверяет на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile("^(https?://)?(www\.)?youtube\.com/.+$")
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError(
                "Ссылка не соответствует требованиям, допустима ссылка только на youtube.com."
            )
