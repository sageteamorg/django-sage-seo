from django import forms
from django.conf import settings
from django.urls import get_resolver

from sage_seo.funcs import collect_view_names


class MetaInformationForm(forms.ModelForm):
    """
    Meta Information of pages
    """

    view_name = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        urlpatterns = get_resolver(None).url_patterns
        # Retrieve the relevant apps from Django settings
        relevant_apps = getattr(settings, "META_INFORMATION_APPS", [])
        view_names = collect_view_names(urlpatterns, relevant_apps)
        self.fields["view_name"].choices = [(name, name) for name in view_names]
