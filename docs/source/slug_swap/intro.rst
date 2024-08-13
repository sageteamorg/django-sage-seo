SlugSwap Feature Documentation
==============================

The SlugSwap feature is a Django model used to manage and record changes in slugs (URL-friendly strings) for different objects. It ensures old URLs redirect to new ones, maintaining SEO and avoiding broken links when slugs are updated.

What does it do?
----------------
- **Manages Slug Changes:** Keeps track of old and new slugs for objects.
- **Redirects URLs:** Automatically redirects users from old URLs to new URLs.
- **SEO Maintenance:** Preserves SEO by ensuring links do not break.

How it works
------------
1. **Slug Management:** An entry in the SlugSwap model maps old slugs to new slugs when an object's slug is updated.
2. **Redirection Middleware:** Middleware intercepts 404 responses, checks for old slugs, and redirects to the new slug using a predefined mapping.
3. **HTTP Status Codes:** Uses either a permanent (301) or temporary (302) redirect based on the redirect_type field.

When should we use it?
----------------------
- **Updating Slugs:** Whenever slugs (and URLs) for objects are updated.
- **SEO Preservation:** To maintain SEO rankings and avoid broken links, preserving user experience and search engine indexing.

How it can improve SEO?
-----------------------
- **Preserves Link Equity:** Ensures any accumulated SEO value is transferred by redirecting old URLs to new ones.
- **Avoids 404 Errors:** Prevents users from encountering broken links, which negatively affect SEO.
- **Maintains User Experience:** Ensures users can still access content via old URLs, crucial for retaining visitors and reducing bounce rates.
