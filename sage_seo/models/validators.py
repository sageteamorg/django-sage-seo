from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_url_format(value):
    """
    Ensure the URL starts and ends with a slash (/).
    """
    if not (value.startswith("/") and value.endswith("/")):
        raise ValidationError(
            _("URL must start and end with a slash (/)."),
            params={"value": value},
        )
