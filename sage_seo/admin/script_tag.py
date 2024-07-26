from django.contrib import admin

from sage_seo.models import ScriptTag


class ScriptTagAdmin(admin.ModelAdmin):

    # Fields to display in the admin change list
    list_display = ("name", "placement", "is_active", "created_at", "modified_at")

    # Enable filtering by these fields
    list_filter = ("placement", "is_active", "created_at")

    # Add search functionality based on these fields
    search_fields = ("name", "content")

    # Make these fields read-only in the change form
    readonly_fields = ("created_at", "modified_at")

    # Group fields in fieldsets for a more organized form layout
    fieldsets = (
        (None, {"fields": ("name", "content", "placement", "is_active")}),
        (
            "Timestamps",
            {
                "fields": ("created_at", "modified_at"),
                "classes": ("collapse",),  # Make this section collapsible
            },
        ),
    )

    # Enable actions to bulk activate or deactivate selected scripts
    actions = ["activate_scripts", "deactivate_scripts"]

    def activate_scripts(self, request, queryset):
        queryset.update(is_active=True)

    activate_scripts.short_description = "Activate selected scripts"

    def deactivate_scripts(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_scripts.short_description = "Deactivate selected scripts"


# Register the model with its custom admin class
admin.site.register(ScriptTag, ScriptTagAdmin)
