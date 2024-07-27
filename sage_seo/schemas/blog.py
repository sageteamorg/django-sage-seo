BLOG_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "@context": {
            "type": "string",
            "default": "https://schema.org",
            "placeholder": "e.g. https://schema.org"
        },
        "@type": {
            "type": "string",
            "default": "ItemList",
            "placeholder": "e.g. ItemList"
        },
        "itemListElement": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "@type": {
                        "type": "string",
                        "default": "BlogPosting",
                        "placeholder": "e.g. BlogPosting"
                    },
                    "headline": {
                        "type": "string",
                        "placeholder": "e.g. Blog Post Title"
                    },
                    "image": {
                        "type": "string",
                        "format": "url",
                        "placeholder": "e.g. https://www.example.com/image.jpg"
                    },
                    "url": {
                        "type": "string",
                        "format": "url",
                        "placeholder": "e.g. https://www.example.com/blog-post"
                    },
                    "datePublished": {
                        "type": "string",
                        "format": "date-time",
                        "placeholder": "e.g. 2024-07-27T00:00:00Z"
                    },
                    "author": {
                        "type": "object",
                        "properties": {
                            "@type": {
                                "type": "string",
                                "default": "Person",
                                "placeholder": "e.g. Person"
                            },
                            "name": {
                                "type": "string",
                                "placeholder": "e.g. Author Name"
                            }
                        }
                    }
                },
                "required": ["headline", "url", "datePublished", "author"]
            }
        }
    }
}


BLOG_DETAIL_SCHEMA = {
    "type": "object",
    "properties": {
        "@context": {
            "type": "string",
            "default": "https://schema.org",
            "placeholder": "e.g. https://schema.org"
        },
        "@type": {
            "type": "string",
            "default": "BlogPosting",
            "placeholder": "e.g. BlogPosting"
        },
        "mainEntityOfPage": {
            "type": "object",
            "properties": {
                "@type": {
                    "type": "string",
                    "default": "WebPage",
                    "placeholder": "e.g. WebPage"
                },
                "@id": {
                    "type": "string",
                    "format": "url",
                    "placeholder": "e.g. https://www.example.com"
                }
            }
        },
        "headline": {
            "type": "string",
            "placeholder": "e.g. Blog Post Title"
        },
        "image": {
            "type": "string",
            "format": "url",
            "placeholder": "e.g. https://www.example.com/image.jpg"
        },
        "datePublished": {
            "type": "string",
            "format": "date-time",
            "placeholder": "e.g. 2024-07-27T00:00:00Z"
        },
        "dateModified": {
            "type": "string",
            "format": "date-time",
            "placeholder": "e.g. 2024-07-28T00:00:00Z"
        },
        "author": {
            "type": "object",
            "properties": {
                "@type": {
                    "type": "string",
                    "default": "Person",
                    "placeholder": "e.g. Person"
                },
                "name": {
                    "type": "string",
                    "placeholder": "e.g. Author Name"
                }
            }
        },
        "publisher": {
            "type": "object",
            "properties": {
                "@type": {
                    "type": "string",
                    "default": "Organization",
                    "placeholder": "e.g. Organization"
                },
                "name": {
                    "type": "string",
                    "placeholder": "e.g. Publisher Name"
                },
                "logo": {
                    "type": "object",
                    "properties": {
                        "@type": {
                            "type": "string",
                            "default": "ImageObject",
                            "placeholder": "e.g. ImageObject"
                        },
                        "url": {
                            "type": "string",
                            "format": "url",
                            "placeholder": "e.g. https://www.example.com/logo.jpg"
                        }
                    }
                }
            }
        },
        "description": {
            "type": "string",
            "placeholder": "e.g. A short description of the blog post"
        },
        "articleBody": {
            "type": "string",
            "placeholder": "e.g. The full text of the blog post"
        }
    },
    "required": ["headline", "datePublished", "author"]
}
