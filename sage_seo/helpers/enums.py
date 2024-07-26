from django.db import models
from django.utils.translation import gettext_lazy as _


class RedirectType(models.TextChoices):
    """
    The RedirectType class defines a model field that stores a
    redirect type as a string, with the options of "primary" or
    "temporary". It is implemented using the models.TextChoices
    class from Django.

    The class has two choices, each represented by
    a tuple with a string value and a human-readable label.
    The first choice is "primary", with a label of "primary".
    The second choice is "temporary", with a label of "temporary".
    These choices can be used to populate a dropdown or radio button in a form.
    """

    Primary = ("primary", _("primary"))
    Temporary = ("temporary", _("temporary"))


class SearchEngineRules(models.TextChoices):
    INDEX = "index", _("Index")
    NOINDEX = "noindex", _("NoIndex")
    FOLLOW = "follow", _("Follow")
    NOFOLLOW = "nofollow", _("NoFollow")
