from django.contrib import admin

from sage_seo.models import SlugSwap


@admin.register(SlugSwap)
class SlugSwapAdmin(admin.ModelAdmin):

    list_display = ("new_slug", "old_slug", "redirect_type", "content_object")

    list_editable = ("redirect_type",)

    readonly_fields = (
        "old_slug",
        "new_slug",
        "content_type",
        "object_id",
        "content_object",
    )

    search_fields = (
        "old_slug",
        "new_slug",
    )
