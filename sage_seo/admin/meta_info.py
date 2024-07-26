from django.contrib import admin

from sage_seo.forms import MetaInformationForm
from sage_seo.models import MetaInformation


@admin.register(MetaInformation)
class MetaInformationAdmin(admin.ModelAdmin):
    form = MetaInformationForm
    save_on_top = True
    fieldsets = (
        (
            "Basic Information",
            {"fields": ("view_name", "title", "canonical_url", "description")},
        ),
        (
            "SEO Settings",
            {
                "fields": (
                    "index_page",
                    "follow_page_links",
                    "keywords",
                    "json_ld",
                ),
                "classes": ("collapse",),
            },
        ),
    )
