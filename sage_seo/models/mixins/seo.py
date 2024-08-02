from django.core.validators import RegexValidator, URLValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from sage_seo.schemas import (BLOG_DETAIL_SCHEMA, BLOG_LIST_SCHEMA,
                              PRODUCT_DETAIL_SCHEMA, PRODUCT_LIST_SCHEMA)

try:
    from django_jsonform.models.fields import JSONField

    JSON_FORMS_AVAILABLE = True
except ImportError:
    JSON_FORMS_AVAILABLE = False


class MetaKeyMixin(models.Model):
    keywords_schema = {"type": "array", "items": {"type": "string"}}

    keywords = JSONField(
        schema=keywords_schema,
        verbose_name=_("SEO Keywords"),
        help_text=_(
            "A list of keywords relevant to the page content, used for SEO purposes."
        ),
        db_comment="List of SEO keywords associated with the page.",
    )

    meta_description = models.TextField(
        verbose_name=_("SEO Description"), null=True, blank=True
    )


class OGMixin(models.Model):
    """
    OGMixin is a model mixin that provides Open Graph (OG) metadata fields for a Django model.

    Open Graph protocol enables any web page to become a rich object in a social graph.
    This is used by social media platforms such as Facebook, LinkedIn, and Twitter to display
    rich media snippets when links are shared. By including these fields in your models, you
    can control how your pages are presented when shared on these platforms.
    """

    og_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("OG Title"),
        help_text=_(
            "The title of the webpage. Example: 'The Amazing Spider-Man - Movie Review'"
        ),
        db_comment="The title of the webpage for Open Graph protocol.",
    )

    og_type = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_("OG Type"),
        help_text=_(
            "The type of the content. Common values: 'website', 'article', 'video', etc. Example: 'article'"
        ),
        db_comment="The type of the content for Open Graph protocol. Common values include 'website', 'article', 'video', etc.",
    )

    og_image = models.URLField(
        null=True,
        blank=True,
        verbose_name=_("OG Image"),
        help_text=_(
            "The URL of the image that represents the webpage. Example: 'https://www.example.com/image.jpg'"
        ),
        validators=[URLValidator()],
        db_comment="The URL of the image that represents the webpage for Open Graph protocol.",
    )

    og_description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("OG Description"),
        help_text=_(
            "A description of the webpage content. Example: 'A comprehensive review of the latest Spider-Man movie, including storyline, character development, and special effects.'"
        ),
        db_comment="A description of the webpage content for Open Graph protocol.",
    )

    og_url = models.URLField(
        null=True,
        blank=True,
        verbose_name=_("OG URL"),
        help_text=_(
            "The URL of the webpage. Example: 'https://www.example.com/page.html'"
        ),
        validators=[URLValidator()],
        db_comment="The URL of the webpage for Open Graph protocol.",
    )

    og_site_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("OG Site Name"),
        help_text=_("The name of the website. Example: 'Example Website'"),
        db_comment="The name of the website for Open Graph protocol.",
    )

    og_locale = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name=_("OG Locale"),
        help_text=_(
            "The locale of the content. Common values: 'en_US', 'fr_FR', etc. Example: 'en_US'"
        ),
        validators=[
            RegexValidator(
                regex=r"^[a-z]{2}_[A-Z]{2}$",
                message=_("Enter a valid locale identifier like en_US"),
            )
        ],
        db_comment="The locale of the content for Open Graph protocol. Example: 'en_US'.",
    )

    article_author = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Article Author"),
        help_text=_("The name of the author of the article. Example: 'John Doe'"),
        db_comment="The name of the author of the article for Open Graph protocol.",
    )

    class Meta:
        abstract = True


class BasicJsonLdMixin(models.Model):
    json_ld = models.JSONField(blank=True, null=True)

    class Meta:
        abstract = True


class ProductListJsonLdMixin(BasicJsonLdMixin):
    json_ld = JSONField(
        schema=PRODUCT_LIST_SCHEMA,
        blank=True,
        null=True,
        help_text=_("Structured JSON-LD data for rich snippets. Enter valid JSON."),
        db_comment="JSON-LD structured data for enhancing search engine listings with rich snippets.",
    )

    class Meta:
        abstract = True


class ProductDetailJsonLdMixin(BasicJsonLdMixin):
    json_ld = JSONField(
        schema=PRODUCT_DETAIL_SCHEMA,
        blank=True,
        null=True,
        help_text=_("Structured JSON-LD data for rich snippets. Enter valid JSON."),
        db_comment="JSON-LD structured data for enhancing search engine listings with rich snippets.",
    )

    class Meta:
        abstract = True


class BlogListJsonLdMixin(BasicJsonLdMixin):
    json_ld = JSONField(
        schema=BLOG_LIST_SCHEMA,
        blank=True,
        null=True,
        help_text=_("Structured JSON-LD data for rich snippets. Enter valid JSON."),
        db_comment="JSON-LD structured data for enhancing search engine listings with rich snippets.",
    )

    class Meta:
        abstract = True


class BlogDetailJsonLdMixin(BasicJsonLdMixin):
    json_ld = JSONField(
        schema=BLOG_DETAIL_SCHEMA,
        blank=True,
        null=True,
        help_text=_("Structured JSON-LD data for rich snippets. Enter valid JSON."),
        db_comment="JSON-LD structured data for enhancing search engine listings with rich snippets.",
    )

    class Meta:
        abstract = True


class SEOMixin(MetaKeyMixin, OGMixin):

    class Meta:
        abstract = True
