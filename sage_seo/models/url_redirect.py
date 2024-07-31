from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from sage_tools.mixins.models.base import TimeStampMixin

from sage_seo.helpers.enums import RedirectType
from sage_seo.models.validators import validate_url_format


class URLRedirect(TimeStampMixin):
    """
    Model to store URL redirection.

    Fields:
        old_url (str): The old URL that was replaced. Must start and end with a slash (/).
        new_url (str): The new URL that replaced the old one. Must start and end with a slash (/).
        redirect_type (str): The HTTP status code used to redirect a user from one URL to another.

    Usage:
        This model is used to map old URLs to new URLs for redirection purposes.
        Both old_url and new_url must be in the format of /example-url/.
    """

    old_url = models.CharField(
        _("Old URL"),
        max_length=255,
        editable=True,
        help_text=_("The old URL that was replaced."),
        validators=[validate_url_format],
    )

    new_url = models.CharField(
        _("New URL"),
        max_length=255,
        editable=True,
        help_text=_("The new URL that replaced the old one."),
        validators=[validate_url_format],
    )

    redirect_type = models.CharField(
        _("Redirect Type"),
        max_length=20,
        validators=[MaxLengthValidator(20)],
        choices=RedirectType.choices,
        default=RedirectType.Primary,
        help_text=_(
            "The HTTP status code used to redirect a user from one URL to another."
        ),
    )

    class Meta:
        verbose_name = _("URL Redirect")
        verbose_name_plural = _("URL Redirects")

    def clean(self):
        super().clean()
        # Check for reverse mapping
        if URLRedirect.objects.filter(
            old_url=self.new_url, new_url=self.old_url
        ).exists():
            raise ValidationError(
                _(
                    "A reverse mapping already exists with old URL '%(old_url)s' and new URL '%(new_url)s'."
                ),
                code="invalid",
                params={"old_url": self.new_url, "new_url": self.old_url},
            )

    def save(self, *args, **kwargs):
        # Run the full clean method
        self.full_clean()
        super().save(*args, **kwargs)
