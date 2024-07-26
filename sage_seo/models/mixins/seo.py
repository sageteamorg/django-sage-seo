from django.db import models
from django.utils.translation import gettext_lazy as _


class SEOMixin(models.Model):
    meta_keywords = models.TextField(
        verbose_name=_("SEO Keywords"),
        default=list,
        null=True,
        blank=True,
    )

    meta_description = models.TextField(
        verbose_name=_("SEO Description"), null=True, blank=True
    )

    json_ld = models.JSONField(blank=True, null=True)

    og_title = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("OG Title")
    )

    og_type = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("OG Type")
    )

    og_image = models.URLField(null=True, blank=True, verbose_name=_("OG Image"))

    og_description = models.TextField(
        null=True, blank=True, verbose_name=_("OG Description")
    )

    twitter_card = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Twitter Card")
    )

    twitter_site = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Twitter Site")
    )

    twitter_creator = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Twitter Creator")
    )

    twitter_image = models.URLField(
        null=True, blank=True, verbose_name=_("Twitter Image")
    )

    class Meta:
        abstract = True
