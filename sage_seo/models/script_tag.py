from django.db import models
from django.utils.translation import gettext_lazy as _
from sage_tools.mixins.models.base import TimeStampMixin

from sage_seo.helpers.choices import ScriptPlacement


class ScriptTag(TimeStampMixin):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Name"),
        help_text=_("Unique name of the script tag."),
        db_comment="Name of the script tag",
    )
    content = models.TextField(
        verbose_name=_("Content"),
        help_text=_("The HTML/JavaScript content to be injected."),
        db_comment="HTML/JavaScript content of the script tag",
    )
    placement = models.CharField(
        max_length=10,
        choices=ScriptPlacement.choices,
        default=ScriptPlacement.HEAD,
        verbose_name=_("Placement"),
        help_text=_("Location in the HTML document where the script will be injected."),
        db_comment="Placement location in the HTML document",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Status to indicate whether the script is active or not."),
        db_comment="Active status of the script tag",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Script Tag")
        verbose_name_plural = _("Script Tags")
        db_table = "script_tag"
        ordering = ["created_at"]
