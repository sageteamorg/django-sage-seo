Meta Key Feature
================

The `MetaInformation` model is designed to store SEO metadata for various views or pages in a Django application. It extends the `TimeStampMixin` to include automatic timestamping features. This model allows for detailed configuration of SEO-related properties such as titles, descriptions, keywords, and structured data in JSON-LD format.

Key Features
------------

- **View Name**: Specifies the view or page this metadata is associated with.
- **Title**: The SEO title of the page.
- **Description**: A brief description of the page content for SEO purposes.
- **Keywords**: A list of relevant keywords for SEO.
- **JSON-LD**: Structured data to enhance search engine listings with rich snippets.
- **Index Page**: Flag to determine if the page should be indexed by search engines.
- **Follow Page Links**: Flag to control whether search engines should follow links on the page.
- **Canonical URL**: The preferred URL to avoid duplicate content issues.
