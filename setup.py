from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django_sage_seo",
    version="0.1.0",
    author="Sepehr Akbarzadeh",
    author_email="sepehr@sageteam.org",
    description="SEO tools for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sageteamorg/django-sage-seo",
    project_urls={
        "Documentation": "https://django-sage-seo.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/sageteamorg/django-sage-seo",
        "Issues": "https://github.com/sageteamorg/django-sage-seo/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.11",
)
