PRODUCT_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "@context": {
            "type": "string",
            "default": "https://schema.org",
            "placeholder": "e.g. https://schema.org",
        },
        "@type": {
            "type": "string",
            "default": "ItemList",
            "placeholder": "e.g. ItemList",
        },
        "itemListElement": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "@type": {
                        "type": "string",
                        "default": "Product",
                        "placeholder": "e.g. Product",
                    },
                    "name": {"type": "string", "placeholder": "e.g. Product Name"},
                    "image": {
                        "type": "string",
                        "format": "url",
                        "placeholder": "e.g. https://www.example.com/product.jpg",
                    },
                    "url": {
                        "type": "string",
                        "format": "url",
                        "placeholder": "e.g. https://www.example.com/product",
                    },
                    "description": {
                        "type": "string",
                        "placeholder": "e.g. Product Description",
                    },
                    "sku": {"type": "string", "placeholder": "e.g. SKU12345"},
                    "brand": {
                        "type": "object",
                        "properties": {
                            "@type": {
                                "type": "string",
                                "default": "Brand",
                                "placeholder": "e.g. Brand",
                            },
                            "name": {
                                "type": "string",
                                "placeholder": "e.g. Brand Name",
                            },
                        },
                    },
                    "offers": {
                        "type": "object",
                        "properties": {
                            "@type": {
                                "type": "string",
                                "default": "Offer",
                                "placeholder": "e.g. Offer",
                            },
                            "priceCurrency": {
                                "type": "string",
                                "placeholder": "e.g. USD",
                            },
                            "price": {"type": "string", "placeholder": "e.g. 19.99"},
                            "itemCondition": {
                                "type": "string",
                                "format": "url",
                                "placeholder": "e.g. https://schema.org/NewCondition",
                            },
                            "availability": {
                                "type": "string",
                                "format": "url",
                                "placeholder": "e.g. https://schema.org/InStock",
                            },
                            "url": {
                                "type": "string",
                                "format": "url",
                                "placeholder": "e.g. https://www.example.com/buy",
                            },
                        },
                    },
                },
            },
        },
    },
}

PRODUCT_DETAIL_SCHEMA = {
    "type": "object",
    "properties": {
        "@context": {
            "type": "string",
            "default": "https://schema.org",
            "placeholder": "e.g. https://schema.org",
        },
        "@type": {
            "type": "string",
            "default": "Product",
            "placeholder": "e.g. Product",
        },
        "name": {"type": "string", "placeholder": "e.g. Product Name"},
        "image": {
            "type": "string",
            "format": "url",
            "placeholder": "e.g. https://www.example.com/product.jpg",
        },
        "description": {"type": "string", "placeholder": "e.g. Product Description"},
        "sku": {"type": "string", "placeholder": "e.g. SKU12345"},
        "brand": {
            "type": "object",
            "properties": {
                "@type": {
                    "type": "string",
                    "default": "Brand",
                    "placeholder": "e.g. Brand",
                },
                "name": {"type": "string", "placeholder": "e.g. Brand Name"},
            },
        },
        "offers": {
            "type": "object",
            "properties": {
                "@type": {
                    "type": "string",
                    "default": "Offer",
                    "placeholder": "e.g. Offer",
                },
                "priceCurrency": {"type": "string", "placeholder": "e.g. USD"},
                "price": {"type": "string", "placeholder": "e.g. 19.99"},
                "itemCondition": {
                    "type": "string",
                    "format": "url",
                    "placeholder": "e.g. https://schema.org/NewCondition",
                },
                "availability": {
                    "type": "string",
                    "format": "url",
                    "placeholder": "e.g. https://schema.org/InStock",
                },
                "url": {
                    "type": "string",
                    "format": "url",
                    "placeholder": "e.g. https://www.example.com/buy",
                },
            },
        },
    },
}
