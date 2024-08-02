import logging

from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


@admin.action(description=_("Reset robots.txt content to default"))
@transaction.atomic
def reset_robots_txt(modeladmin, request, queryset):
    # Ensure only one instance is affected
    if queryset.count() != 1:
        modeladmin.message_user(
            request,
            _("Action cannot be performed on multiple instances."),
            level="error",
        )
        raise PermissionDenied(_("Action cannot be performed on multiple instances."))

    try:
        queryset.update(content="User-agent: *\nDisallow: /")
        modeladmin.message_user(
            request, _("Selected robots.txt content has been reset.")
        )
        logger.info(f"Robots.txt content reset by {request.user}.")
    except Exception as e:
        modeladmin.message_user(
            request, _("An error occurred while resetting the content."), level="error"
        )
        logger.error(f"Error resetting robots.txt content: {e}")
        raise
