URL Redirect
============

The URL Redirect Middleware is a custom middleware for Django applications designed to handle URL redirection based on database entries. It intercepts HTTP requests that result in a 404 error (page not found) and checks if there is a corresponding new URL in the database. If a mapping exists, it redirects the user to the new URL.

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    intro