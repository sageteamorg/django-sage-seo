from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SeoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sage_seo"
    verbose_name = _("Search Engine Optimization")
