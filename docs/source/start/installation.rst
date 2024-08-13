Installation
============

This section will guide you through the installation process for Django Sage SEO. Follow these steps to get started.

Creating a Virtual Environment
------------------------------

Creating a virtual environment is an important best practice in Python development. It helps you manage dependencies and avoid conflicts between different projects. To create a virtual environment, use the following commands:

Using ``venv`` (Python's built-in tool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    python -m venv myenv
    source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`

Using ``virtualenv`` (third-party tool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, install ``virtualenv`` if you haven't already:

::

    pip install virtualenv

Then, create and activate a virtual environment:

::

    virtualenv myenv
    source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`

Installing Django Sage SEO
---------------------------

There are two primary ways to install Django Sage SEO: using ``pip`` or ``poetry``.

Using ``pip``
~~~~~~~~~~~~~

To install Django Sage SEO using ``pip``, run the following command in your terminal:

::

    pip install django-sage-seo

Using ``poetry``
~~~~~~~~~~~~~~~~

If you prefer using ``poetry`` for dependency management, add Django Sage SEO to your project with the following command:

::

    poetry add django-sage-seo

Adding Django Sage SEO to Installed Apps
-----------------------------------------

After installing Django Sage SEO, add it to your ``INSTALLED_APPS`` in your Django settings file:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        "sage_seo",
        "django_jsonform"
        ...
    ]


Running Migrations
------------------

Run the following command to create the necessary database tables:

::

    python manage.py makemigrations
    python manage.py migrate

Verifying Installation
----------------------

Start your Django development server and navigate to the admin panel. You should see the Django Sage SEO models available for management. You are now ready to start using Django Sage SEO!
