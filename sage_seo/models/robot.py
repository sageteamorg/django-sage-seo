from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from sage_tools.mixins.models import TimeStampMixin, SingletonModelMixin


class RobotsTxt(SingletonModelMixin, TimeStampMixin):
    content = models.TextField()

    class Meta:
        verbose_name = _("Robots.txt")
        verbose_name_plural = _("Robots.txt")

    def __str__(self):
        return "Robots.txt Content"
