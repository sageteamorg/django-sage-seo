import html
import json
import secrets
import string

from django.urls import URLPattern, URLResolver
from django.views.generic import DetailView
from django.utils.safestring import mark_safe

from sage_seo.helpers.enums import SearchEngineRules


def get_meta_info(view_name):
    """
    Retrieve MetaInformation instance based on the processed view_name.

    Returns:
        MetaInformation: An instance of MetaInformation or None if not found.
    """
    from sage_seo.models import MetaInformation

    # Check if ':' exists in the view_name and process accordingly
    if ":" in view_name:
        processed_view_name = view_name.split(":", 1)[1].replace("-", " ").title()
    else:
        processed_view_name = view_name.replace("-", " ").title()

    try:
        meta_info_instance = MetaInformation.objects.filter(
            view_name__istartswith=processed_view_name
        ).first()
    except MetaInformation.DoesNotExist:
        meta_info_instance = None

    return meta_info_instance


def build_robots_meta(index_page, follow_page_links):
    """Construct content value for the robots meta tag."""
    return ", ".join(
        [
            SearchEngineRules.INDEX if index_page else SearchEngineRules.NOINDEX,
            (
                SearchEngineRules.FOLLOW
                if follow_page_links
                else SearchEngineRules.NOFOLLOW
            ),
        ]
    )


def build_json_ld(json_ld):
    """Return a script tag with JSON-LD data if present."""
    if json_ld:
        json_ld_data = json.dumps(json_ld)
        # Mark the JSON-LD data as safe for HTML output
        return mark_safe(f'<script type="application/ld+json">{json_ld_data}</script>')
    return ""


def generate_short_code():
    length = 6  # Length of the short code
    # Generate a cryptographically secure random string of the specified length
    return "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def collect_view_names(patterns, app_names):
    view_names = []
    for pattern in patterns:
        if isinstance(pattern, URLPattern):
            view_func = pattern.callback
            view_module = view_func.__module__
            # Exclude admin views
            if "admin" in view_module:
                continue
            if hasattr(view_func, "view_class"):
                # Check if the view is a DetailView or a subclass thereof
                if issubclass(view_func.view_class, DetailView):
                    continue  # Skip if the view is a DetailView
            if any(app_name in view_module for app_name in app_names):
                view_name = (
                    f'{pattern.name.replace("-", " ").title()} | {pattern.lookup_str}'
                )
                view_names.append(view_name)
        elif isinstance(pattern, URLResolver):
            view_names.extend(collect_view_names(pattern.url_patterns, app_names))
    return view_names
