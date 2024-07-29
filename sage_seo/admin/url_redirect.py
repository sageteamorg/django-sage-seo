from django.contrib import admin

from ..models import URLRedirect


@admin.register(URLRedirect)
class URLRedirectAdmin(admin.ModelAdmin):
    list_display = ("old_url", "new_url", "redirect_type")

    list_editable = ("redirect_type",)

    search_fields = (
        "old_url",
        "new_url",
    )

    readonly_fields = ("created_at", "modified_at")

    fieldsets = (
        (None, {"fields": ("old_url", "new_url", "redirect_type")}),
        (
            "Timestamps",
            {
                "fields": ("created_at", "modified_at"),
                "classes": ("collapse",),  # Make this section collapsible
            },
        ),
    )
