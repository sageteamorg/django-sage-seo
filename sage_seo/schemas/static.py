STATIC_SCHEMA = {
    "type": "object",
    "properties": {
        "@context": {
            "type": "string",
            "default": "https://schema.org",
            "placeholder": "e.g. https://schema.org"
        },
        "@type": {
            "type": "string",
            "enum": [
                "AboutPage",
                "ArchiveComponent",
                "CheckoutPage",
                "CollectionPage",
                "ContactPage",
                "FAQPage",
                "ItemPage",
                "MedicalWebPage",
                "ProfilePage",
                "QAPage",
                "RealEstateListing",
                "SearchResultsPage",
                "WebPage"
            ],
            "default": "ContactPage",
            "placeholder": "e.g. ContactPage"
        },
        "name": {
            "type": "string",
            "placeholder": "e.g. My Organization"
        },
        "url": {
            "type": "string",
            "format": "url",
            "placeholder": "e.g. https://www.example.com"
        },
        "description": {
            "type": "string",
            "placeholder": "e.g. A short description of the page"
        },
        "image": {
            "type": "string",
            "format": "url",
            "placeholder": "e.g. https://www.example.com/image.jpg"
        },
        "mainEntity": {
            "type": "object",
            "properties": {
                "@type": {
                    "type": "string",
                    "enum": [
                        "Organization",
                        "Corporation",
                        "EducationalOrganization",
                        "GovernmentOrganization",
                        "NGO",
                        "PerformingGroup",
                        "SportsOrganization",
                        "LocalBusiness",
                        "MedicalOrganization",
                        "NewsMediaOrganization",
                        "Project",
                        "Airline",
                        "AnimalShelter",
                        "ArchiveOrganization",
                        "AutomotiveBusiness",
                        "ChildCare",
                        "Dentist",
                        "DryCleaningOrLaundry",
                        "EmergencyService",
                        "EmploymentAgency",
                        "EntertainmentBusiness",
                        "FinancialService",
                        "FoodEstablishment",
                        "GovernmentService",
                        "HealthAndBeautyBusiness",
                        "HomeAndConstructionBusiness",
                        "InternetCafe",
                        "LegalService",
                        "Library",
                        "LodgingBusiness",
                        "MedicalBusiness",
                        "ProfessionalService",
                        "RadioStation",
                        "RealEstateAgent",
                        "RecyclingCenter",
                        "SelfStorage",
                        "ShoppingCenter",
                        "Store",
                        "TelevisionStation",
                        "TouristInformationCenter",
                        "TravelAgency"
                    ],
                    "default": "Organization",
                    "placeholder": "e.g. Organization"
                },
                "name": {
                    "type": "string",
                    "placeholder": "e.g. Example Organization"
                },
                "url": {
                    "type": "string",
                    "format": "url",
                    "placeholder": "e.g. https://www.organization.com"
                },
                "logo": {
                    "type": "string",
                    "format": "url",
                    "placeholder": "e.g. https://www.organization.com/logo.png"
                },
                "sameAs": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "format": "url",
                        "placeholder": "e.g. https://www.linkedin.com/company/organization"
                    }
                },
                "contactPoint": {
                    "type": "object",
                    "properties": {
                        "@type": {
                            "type": "string",
                            "default": "ContactPoint",
                            "placeholder": "e.g. ContactPoint"
                        },
                        "telephone": {
                            "type": "string",
                            "placeholder": "e.g. +1-800-555-5555"
                        },
                        "contactType": {
                            "type": "string",
                            "placeholder": "e.g. Customer Support"
                        },
                        "areaServed": {
                            "type": "string",
                            "placeholder": "e.g. Global"
                        },
                        "availableLanguage": {
                            "type": "string",
                            "placeholder": "e.g. English"
                        }
                    }
                },
                "address": {
                    "type": "object",
                    "properties": {
                        "@type": {
                            "type": "string",
                            "default": "PostalAddress",
                            "placeholder": "e.g. PostalAddress"
                        },
                        "streetAddress": {
                            "type": "string",
                            "placeholder": "e.g. 1234 Main St"
                        },
                        "addressLocality": {
                            "type": "string",
                            "placeholder": "e.g. Anytown"
                        },
                        "addressRegion": {
                            "type": "string",
                            "placeholder": "e.g. CA"
                        },
                        "postalCode": {
                            "type": "string",
                            "placeholder": "e.g. 12345"
                        },
                        "addressCountry": {
                            "type": "string",
                            "placeholder": "e.g. USA"
                        }
                    }
                },
                "geo": {
                    "type": "object",
                    "properties": {
                        "@type": {
                            "type": "string",
                            "default": "GeoCoordinates",
                            "placeholder": "e.g. GeoCoordinates"
                        },
                        "latitude": {
                            "type": "number",
                            "placeholder": "e.g. 37.4224764"
                        },
                        "longitude": {
                            "type": "number",
                            "placeholder": "e.g. -122.0842499"
                        }
                    }
                }
            }
        }
    },
    "required": ["name", "url"]
}