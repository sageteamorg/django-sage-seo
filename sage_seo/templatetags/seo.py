import json
import logging

from django import template
from django.conf import settings
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

from sage_seo.funcs import build_json_ld, build_robots_meta, get_meta_info

logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def render_meta_tags(view_name):
    try:
        meta_info = get_meta_info(view_name)
    except IndexError:
        return ""

    if not meta_info:
        return ""

    if isinstance(meta_info.keywords, list):
        meta_keyword_tag = format_html(
            '<meta name="keywords" content="{}">', escape(",".join(meta_info.keywords))
        )
    elif isinstance(meta_info.keywords, str):
        meta_keyword_tag = format_html(
            '<meta name="keywords" content="{}">', escape(meta_info.keywords)
        )
    else:
        meta_keyword_tag = format_html('<meta name="keywords" content="">')

    meta_tags = [
        format_html("<title>{}</title>", escape(meta_info.title)),
        format_html(
            '<meta name="description" content="{}">', escape(meta_info.description)
        ),
        meta_keyword_tag,
        format_html(
            '<meta name="robots" content="{}">',
            escape(
                build_robots_meta(meta_info.index_page, meta_info.follow_page_links)
            ),
        ),
    ]

    if meta_info.canonical_url:
        meta_tags.append(
            format_html(
                '<link rel="canonical" href="{}" />', escape(meta_info.canonical_url)
            )
        )

    json_ld_script = build_json_ld(meta_info.json_ld)
    if json_ld_script:
        meta_tags.append(json_ld_script)

    # Join the tags and mark the entire string as safe
    return mark_safe("".join(meta_tags))


@register.simple_tag
def render_detail_meta_tags(obj):
    # Initialize an empty list to store meta tags
    meta_tags = []

    meta_tags.append(format_html("<title>{}</title>", escape(obj.title)))

    # Check for each attribute and if it exists, create the corresponding meta tag
    if getattr(obj, "meta_keywords", None):
        keywords = escape(",".join(obj.meta_keywords))
        meta_tags.append(format_html('<meta name="keywords" content="{}">', keywords))

    if getattr(obj, "meta_description", None):
        meta_tags.append(
            format_html(
                '<meta name="description" content="{}">', escape(obj.meta_description)
            )
        )

    if getattr(obj, "json_ld", None):
        json_ld_data = escape(json.dumps(obj.json_ld))
        json_ld_script = format_html(
            '<script type="application/ld+json">{}</script>', json_ld_data
        )
        meta_tags.append(json_ld_script)

    if getattr(obj, "og_title", None):
        meta_tags.append(
            format_html('<meta property="og:title" content="{}">', escape(obj.og_title))
        )

    if getattr(obj, "og_type", None):
        meta_tags.append(
            format_html('<meta property="og:type" content="{}">', escape(obj.og_type))
        )

    if getattr(obj, "og_image", None):
        meta_tags.append(
            format_html(
                '<meta property="og:image" content="{}">', escape(obj.og_image.url)
            )
        )

    if getattr(obj, "og_description", None):
        meta_tags.append(
            format_html(
                '<meta property="og:description" content="{}">',
                escape(obj.og_description),
            )
        )

    if getattr(obj, "twitter_card", None):
        meta_tags.append(
            format_html(
                '<meta name="twitter:card" content="{}">', escape(obj.twitter_card)
            )
        )

    if getattr(obj, "twitter_site", None):
        meta_tags.append(
            format_html(
                '<meta name="twitter:site" content="{}">', escape(obj.twitter_site)
            )
        )

    if getattr(obj, "twitter_creator", None):
        meta_tags.append(
            format_html(
                '<meta name="twitter:creator" content="{}">',
                escape(obj.twitter_creator),
            )
        )

    if getattr(obj, "twitter_image", None):
        meta_tags.append(
            format_html(
                '<meta name="twitter:image" content="{}">',
                escape(obj.twitter_image.url),
            )
        )

    # Optionally, handle the canonical URL if it's a detail page
    domain = settings.DOMAIN_URL
    try:
        canonical_url = escape(f"https://{domain}{obj.get_absolute_url()}")
        meta_tags.append(
            format_html('<link rel="canonical" href="{}" />', canonical_url)
        )
    except AttributeError as e:
        logger.debug(e, exc_info=True)

    # Join the tags and mark the entire string as safe
    return mark_safe("".join(meta_tags))
