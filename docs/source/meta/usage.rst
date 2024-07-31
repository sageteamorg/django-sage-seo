Usage
-----

The `MetaInformation` model is utilized to improve the SEO of a Django application by providing detailed metadata for each page. This metadata is crucial for search engines to understand the content and relevance of the page, which can improve search rankings and visibility.

Example Usage
~~~~~~~~~~~~~

Here's an example of how you might use the `MetaInformation` model:

.. code-block:: python

    from myapp.models import MetaInformation

    meta_info = MetaInformation.objects.create(
        view_name='homepage',
        title='Home - My Awesome Site',
        description='Welcome to the homepage of My Awesome Site, where you can find amazing content.',
        keywords=['home', 'awesome site', 'amazing content'],
        json_ld={
            "@context": "http://schema.org",
            "@type": "WebSite",
            "name": "My Awesome Site",
            "url": "http://www.myawesomesite.com"
        },
        index_page=True,
        follow_page_links=True,
        canonical_url='http://www.myawesomesite.com'
    )

**Attribute Details**
---------------------

The following table provides details on each attribute of the `MetaInformation` model and their SEO benefits:


+---------------------+-------------------------------------------------------+------------------------------------------------------------------------+
| Attribute           | Description                                           |   SEO Benefit                                                          |
+=====================+=======================================================+========================================================================+
|   view_name         | The name of the view or page this meta information    | Helps in associating SEO metadata with specific pages.                 |
|                     | applies to.                                           |                                                                        |
+---------------------+-------------------------------------------------------+------------------------------------------------------------------------+
|   title             | The title of the page for SEO purposes.               | Improves the search engine ranking by providing a relevant title.      |
+---------------------+-------------------------------------------------------+------------------------------------------------------------------------+
|   description       | A brief description of the page content for SEO       | Enhances the search snippet shown in search results, improving         |
|                     | purposes.                                             | click-through rates.                                                   |
+---------------------+-------------------------------------------------------+------------------------------------------------------------------------+
|   keywords          | A list of keywords relevant to the page content.      | Assists search engines in understanding the primary topics of the page.|
+---------------------+-------------------------------------------------------+------------------------------------------------------------------------+
|   json_ld           | Structured JSON-LD data for rich snippets.            | Enables rich snippets in search results, which can increase visibility |
|                     |                                                       | and click-through rates.                                               |
+---------------------+-------------------------------------------------------+------------------------------------------------------------------------+
|   index_page        | Indicates whether search engines should index this    | Controls whether the page appears in search results, useful for        |
|                     | page.                                                 | managing duplicate content.                                            |
+---------------------+-------------------------------------------------------+------------------------------------------------------------------------+
|   follow_page_links | Determines if search engine crawlers should follow    | Helps in distributing link equity to other pages, enhancing overall    |
|                     | links on this page.                                   | site SEO.                                                              |
+---------------------+-------------------------------------------------------+------------------------------------------------------------------------+
|   canonical_url     | The preferred URL for this page to avoid duplicate    | Prevents SEO issues related to duplicate content by consolidating link |
|                     | content issues.                                       | equity.                                                                |
+---------------------+-------------------------------------------------------+------------------------------------------------------------------------+

**How `view_name` Works**
-------------------------

The `view_name` field in the `MetaInformation` model is dynamically populated with choices representing the available views in the Django application. This is achieved through the `MetaInformationForm` class, which retrieves and processes URL patterns to collect view names.

.. note::

    The relevant applications are specified in the Django settings under the key `META_INFORMATION_APPS`. This setting should be a list of application names that you want to include in the view name choices.

.. code-block:: python

    # settings.py
    META_INFORMATION_APPS = [
      'app1',
      'app2',
    ]

.. important::

    Ensure that `META_INFORMATION_APPS` in your settings file includes only those apps where you need SEO metadata management. This helps in keeping the choices list clean and relevant.

This process ensures that only relevant and specific views are available for selection in the admin interface, streamlining the SEO management process for different pages.

**Conclusion**
--------------

The `MetaInformation` model and its corresponding admin configuration provide a robust way to manage SEO metadata for a Django application. By using this model, developers can enhance the search engine visibility and ranking of their site's pages, ultimately driving more traffic and improving user engagement.
