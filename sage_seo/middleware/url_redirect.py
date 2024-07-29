import logging
import re
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.urls import resolve, Resolver404

from ..models import URLRedirect
from ..helpers.enums import RedirectType

logger = logging.getLogger(__name__)


class URLRedirectMiddleware(MiddlewareMixin):
    """
    Middleware to handle URL redirection based on database entries.

    This middleware intercepts responses with a 404 status code,
    checks if there is a mapping for the requested URL in the `URLRedirect` model,
    and if found, redirects the user to the new URL.
    This is useful for managing URL changes and ensuring that users and search engines are redirected to the
    correct pages without encountering broken links.

    """

    def __init__(self, get_response):
        """
        This method sets up the middleware by storing the get_response function,
        which represents the next middleware or view to be called.
        The super() call ensures proper initialization of the base class.
        """
        self.get_response = get_response
        super().__init__(get_response)

    def process_response(self, request, response):
        """
        This method checks if the response has a 404 status code,
        indicating that the requested URLwas not found.
        If a 404 is detected, it attempts to find a new URL for the requested old URLusing the `get_new_url` method.
        If a mapping is found, it returns a permanent redirect response to the new URL.
        """
        old_url = request.path

        # Check for 404 status code
        if response.status_code == 404:
            new_url = self.get_new_url(old_url)
            if new_url:
                # Redirect to the new URL
                return HttpResponsePermanentRedirect(new_url)

        return response

    def url_exists_in_urlpatterns(self, url):
        """
        This method attempts to resolve the given URL using Django's URL resolver.
        If the URL can be resolved without raising a `Resolver404` exception,
        it returns True, indicating that the URL exists in the current URL patterns.
        """
        try:
            resolve(url)
            return True
        except Resolver404:
            return False

    def get_new_url(self, old_url):
        """
        This method queries the `URLRedirect` model to find a mapping for the given old URL.
        If a mapping exists, it returns the new URL. If no mapping is found, it returns None.
        """
        try:
            url_mapping = URLRedirect.objects.get(old_url=old_url)
            return url_mapping.new_url
        except URLRedirect.DoesNotExist:
            return None
