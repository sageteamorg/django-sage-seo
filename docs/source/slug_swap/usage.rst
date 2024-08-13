Using SlugSwap in Django
========================

To utilize the SlugSwap feature in your Django project, follow these steps:

1. **Create the SlugSwap Model:**

   Ensure the ``SlugSwap`` model is defined in your Django app to keep track of old and new slugs for objects.

2. **Define the Middleware:**

   Implement the middleware to handle old slug redirection.

3. **Configure Settings:**

   Add the middleware to your Django settings and configure the ``SLUG_TYPE_MAPPING``:

   .. code-block:: python

       MIDDLEWARE = [
           # other middlewares...
           'your_app.middleware.OldSlugRedirectMiddleware',
       ]

       SLUG_TYPE_MAPPING = {
           'product_slug': 'product',
           'category_slug': 'category',
           'post_slug': 'post',
           'slug': 'other',
       }

   .. warning::

      The keys in ``SLUG_TYPE_MAPPING`` must match the slug names defined in your views. The values should be the models where these slugs are present. If the keys do not match the slugs in your URLs, the redirection will not work.

   Ensure that the slug names in your URLs are used as keys and the corresponding models containing these slugs are used as values.

   For example, if you have a URL pattern like:

   .. code-block:: python

       path('product/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product-detail')

   You should have an entry in ``SLUG_TYPE_MAPPING`` as follows:

   .. code-block:: python

       SLUG_TYPE_MAPPING = {
           'product_slug': 'product',
           # other mappings...
       }

4. **Migrate Database:**

   Create and apply migrations for the ``SlugSwap`` model:

   .. code-block:: bash

       python manage.py makemigrations
       python manage.py migrate

By following these steps, the ``SlugSwap`` feature will be integrated into your Django project, allowing for seamless redirection of old URLs to new ones.
