"""
Public Pages Context Processor
"""

from typing import Any

from django.http import HttpRequest

from sage_seo.helpers.choices import ScriptPlacement
from sage_seo.models import ScriptTag


def get_seo_context(request: HttpRequest) -> dict[Any]:
    view_name = request.resolver_match.view_name if request.resolver_match else ""
    scripts_head = ScriptTag.objects.filter(
        is_active=True, placement=ScriptPlacement.HEAD
    )
    scripts_start_body = ScriptTag.objects.filter(
        is_active=True, placement=ScriptPlacement.START_BODY
    )
    scripts_end_body = ScriptTag.objects.filter(
        is_active=True, placement=ScriptPlacement.END_BODY
    )

    context = {
        "view_name": view_name,
        "scripts_head": scripts_head,
        "scripts_start_body": scripts_start_body,
        "scripts_end_body": scripts_end_body,
    }
    return context
