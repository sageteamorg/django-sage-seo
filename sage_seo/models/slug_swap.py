from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from sage_seo.helpers.enums import RedirectType


class SlugSwap(models.Model):
    """
    The SlugSwap model is used to manage and record the changes in slugs for different
    objects. It helps in redirecting old URLs to new ones, thereby maintaining SEO and
    ensuring that links do not break when slugs are updated.

    Example of usage:
        When an object's slug is updated, an entry in SlugSwap can be created to map the old slug
        to the new slug. This allows for automatic redirection from the old URL to the new URL.

    """
    old_slug = models.SlugField(
        _("Old Slug"),
        max_length=255,
        editable=False,
        allow_unicode=True,
        help_text=_(
            "Slug is a newspaper term. A short label for "
            "something containing only letters, numbers, underscores, "
            "or hyphens. They are generally used in URLs."
        ),
    )

    new_slug = models.SlugField(
        _("New Slug"),
        max_length=255,
        editable=False,
        allow_unicode=True,
        help_text=_(
            "Slug is a newspaper term. A short label for "
            "something containing only letters, numbers, underscores, "
            "or hyphens. They are generally used in URLs."
        ),
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        help_text=_("Content type of the related object."),
    )
    object_id = models.PositiveIntegerField(help_text=_("ID of the related object."))
    content_object = GenericForeignKey("content_type", "object_id")

    redirect_type = models.CharField(
        _("redirect type"),
        max_length=20,
        validators=[MaxLengthValidator(20)],
        choices=RedirectType.choices,
        default=RedirectType.Primary,
        help_text=_(
            "refers to the HTTP status code that is used to"
            "redirect a user from one URL to another"
        ),
    )

    class Meta:
        verbose_name = _("Slug Swap")
        verbose_name_plural = _("Slug Swaps")
