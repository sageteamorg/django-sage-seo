import logging
from django.urls import reverse, NoReverseMatch
from django.utils.deprecation import MiddlewareMixin
from django.http import (
    Http404,
    HttpResponseRedirect as TemporaryRedirect,
    HttpResponsePermanentRedirect as PermanentRedirect
)
from django.conf import settings
from sage_seo.models import SlugSwap
from sage_seo.helpers.enums import RedirectType

logger = logging.getLogger(__name__)


class OldSlugRedirectMiddleware(MiddlewareMixin):
    """
    Middleware to handle old slug redirection.

    This middleware intercepts 404 responses and checks if the requested URL slug has
    been changed. If an old slug is detected, it attempts to find the new slug and
    redirects the user to the updated URL.

    The middleware uses the `SLUG_TYPE_MAPPING` setting to determine the mappings
    between URL parameter names and their respective content types. If a mapping is found,
    it updates the URL parameters and performs a redirect based on the new slug information.

    Example of SLUG_TYPE_MAPPING in settings:
    SLUG_TYPE_MAPPING = {
        'product_slug': 'product',
        'category_slug': 'category',
        'post_slug': 'post',
        'slug': 'other',
    }

    The middleware performs the following steps:
    1. Intercepts 404 responses.
    2. Retrieves the old slug from the request.
    3. Uses the mapping defined in SLUG_TYPE_MAPPING to find the new slug.
    4. Constructs the new URL and redirects the user.
    5. Logs any errors encountered during the process.

    This helps maintain SEO and user experience by ensuring that outdated links
    continue to direct users to the correct content.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        super().__init__(get_response)

    def process_response(self, request, response):
        """
        Processes the response to check for 404 errors and handle old slug redirection.

        This method intercepts 404 responses, checks for old slugs in the request,
        and attempts to find and redirect to the new slug using the SLUG_TYPE_MAPPING
        settings.

        If the requested URL matches an old slug, the method constructs a new URL
        with the updated slug and performs a redirect to the new URL.

        """
        if response.status_code == 404:
            try:
                updated_kwargs = {}

                for slug_name, slug_type in settings.SLUG_TYPE_MAPPING.items():
                    old_slug = request.resolver_match.kwargs.get(slug_name)
                    if old_slug:
                        updated_kwargs[slug_name] = self._get_new_slug(old_slug, slug_type)

                if updated_kwargs:
                    try:
                        new_url = reverse(request.resolver_match.view_name, kwargs=updated_kwargs)
                        return self._redirect(new_url, updated_kwargs)
                    except NoReverseMatch as e:
                        logger.error(f'NoReverseMatch: {e} for view {request.resolver_match.view_name} with kwargs {updated_kwargs}')
                        raise Http404('Page not found.')

            except AttributeError as e:
                logger.warning(f'AttributeError: {e} in OldSlugRedirectMiddleware')
            except Exception as e:
                logger.error(f'Unexpected error: {e} in OldSlugRedirectMiddleware')

        return response

    def _get_new_slug(self, old_slug, slug_type):
        """
        Retrieves the new slug for the given old slug and content type.

        This method checks if there is a new slug associated with the given old slug
        and content type. If a new slug is found, it is returned; otherwise, the old
        slug is returned.
        """
        try:
            slug_swap = SlugSwap.objects.filter(old_slug=old_slug, content_type__model=slug_type).first()
            if slug_swap:
                return slug_swap.new_slug
            return old_slug
        except SlugSwap.DoesNotExist:
            return old_slug
        except Exception as e:
            logger.error(f'Error retrieving new slug for {old_slug} of type {slug_type}: {e}')
            return old_slug

    def _redirect(self, url, updated_kwargs):
        """
        Redirects to the new URL based on the updated slug.

        This method performs a redirection to the new URL constructed with the updated
        slug. It determines whether to perform a permanent or temporary redirect based
        on the redirect type defined in the SlugSwap model.

        """
        try:
            slug_swap = SlugSwap.objects.filter(
                old_slug=updated_kwargs.get('product_slug') or
                updated_kwargs.get('post_slug') or
                updated_kwargs.get('category_slug') or
                updated_kwargs.get('slug')
            ).first()
            if slug_swap:
                if slug_swap.redirect_type == RedirectType.Primary:
                    return PermanentRedirect(url)
                else:
                    return TemporaryRedirect(url)
            return TemporaryRedirect(url)
        except Exception as e:
            logger.error(f'Error during redirect to {url} with kwargs {updated_kwargs}: {e}')
            return TemporaryRedirect(url)
