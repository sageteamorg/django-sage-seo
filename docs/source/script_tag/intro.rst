ScriptTag Model Purpose
=======================

The ``ScriptTag`` model is designed to manage HTML/JavaScript content within a Django application for SEO purposes. This model enables users to define script tags that can be dynamically injected into specified locations of an HTML document.

Key attributes include:
- ``name``: A unique identifier for each script tag.
- ``content``: The actual HTML/JavaScript code to be inserted.
- ``placement``: Specifies where in the HTML document the script should be placed, such as in the head or body.
- ``is_active``: Indicates whether the script tag is currently active and should be injected.

Examples
--------

1. **Adding a Google Analytics Script**

   To add a Google Analytics script, you can create an instance of the ``ScriptTag`` model in your Django application:

   .. code-block:: python

      from sage_seo.models import ScriptTag

      google_analytics_script = ScriptTag(
          name='google_analytics',
          content="""
          <script async src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXXX-X"></script>
          <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'UA-XXXXXX-X');
          </script>
          """,
          placement='head',
          is_active=True
      )
      google_analytics_script.save()

2. **Adding a Chat Widget Script**

   Similarly, to add a chat widget script, create another instance of the ``ScriptTag`` model:

   .. code-block:: python

      from sage_seo.models import ScriptTag

      chat_widget_script = ScriptTag(
          name='chat_widget',
          content="""
          <script>
            (function(w, d, s, u) {
              w.ChatWidgetID = '12345';
              var h = d.getElementsByTagName('head')[0];
              var j = d.createElement('script'); j.async = true; j.src = u;
              h.appendChild(j);
            })(window, document, 'script', 'https://example.com/chat.js');
          </script>
          """,
          placement='body',
          is_active=True
      )
      chat_widget_script.save()

This model allows for efficient management and customization of scripts, enhancing the SEO capabilities of the application by facilitating the dynamic insertion of essential tags in desired locations.
