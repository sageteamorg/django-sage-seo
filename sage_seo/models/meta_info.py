from django.db import models
from django.utils.translation import gettext_lazy as _
from sage_tools.mixins.models.base import TimeStampMixin


class MetaInformation(TimeStampMixin):
    view_name = models.CharField(
        max_length=255,
        verbose_name=_("View Name"),
        help_text=_("The name of the view or page this meta information applies to."),
        db_comment="The view or route name associated with this meta information.",
    )

    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
        help_text=_("The title of the page for SEO purposes."),
        db_comment="SEO title of the page.",
    )

    description = models.CharField(
        max_length=160,
        verbose_name=_("Description"),
        help_text=_(
            "A brief description of the page content for SEO purposes. Ideally 155 to 160 characters."
        ),
        db_comment="SEO description of the page, used in search engine listings.",
    )

    keywords = models.TextField(
        default=list,
        verbose_name=_("SEO Keywords"),
        help_text=_(
            "A list of keywords relevant to the page content, used for SEO purposes."
        ),
        db_comment="List of SEO keywords associated with the page.",
    )

    index_page = models.BooleanField(
        default=True,
        help_text=_("Indicates whether search engines should index this page."),
        db_comment="Flag indicating if the page should be indexed by search engines.",
    )

    follow_page_links = models.BooleanField(
        default=True,
        help_text=_(
            "Determines if search engine crawlers should follow links on this page. 'True' allows following links, enhancing link equity distribution."
        ),
        db_comment="Controls whether search engine crawlers are advised to follow links found on this page.",
    )

    json_ld = models.JSONField(
        blank=True,
        null=True,
        help_text=_("Structured JSON-LD data for rich snippets. Enter valid JSON."),
        db_comment="JSON-LD structured data for enhancing search engine listings with rich snippets.",
    )

    canonical_url = models.URLField(
        unique=True,
        verbose_name=_("Canonical URL"),
        help_text=_(
            "The preferred URL for this page, used to avoid duplicate content issues."
        ),
        db_comment="Canonical URL of the page to prevent SEO issues related to duplicate content.",
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
