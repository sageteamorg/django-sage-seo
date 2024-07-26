from django.db import models
from django.utils.translation import gettext_lazy as _


class ScriptPlacement(models.TextChoices):
    HEAD = "head", _("Head")
    START_BODY = "start_body", _("Start of Body")
    END_BODY = "end_body", _("End of Body")
