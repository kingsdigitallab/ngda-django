from django.conf import settings
from django.conf.urls import include, url
from django.core.paginator import Paginator
from django.contrib import admin

from archives import urls as archive_urls

from kdl_ldap.signal_handlers import \
    register_signal_handlers as kdl_ldap_register_signal_hadlers


# For overriding haystack search:
from haystack.forms import FacetedSearchForm
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView


# Now create your own that subclasses the base view
class FacetedSearchView(BaseFacetedSearchView):
    form_class = FacetedSearchForm
    facet_fields = ['genre', 'artist', 'buyer', 'seller']
    template_name = 'search/facet_search.html'
    context_object_name = 'page_object'
    sort = ['stock_number']
    paginate_by = 50
    paginate_orphans = 0
    paginator_class = Paginator


kdl_ldap_register_signal_hadlers()


admin.autodiscover()


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^wagtail/', include(wagtailadmin_urls)),
    # url(r'^documents/', include(wagtaildocs_urls)),
    # url(r'^search/', include(wagtailsearch_frontend_urls)),
    url(r'^search/', include('haystack.urls')),
    url(r'^facet/', FacetedSearchView.as_view(), name='haystack_search'),
    # url(r'', include(wagtail_urls)),
    url(r'', include(archive_urls)),
]

# -----------------------------------------------------------------------------
# Django Debug Toolbar URLS
# -----------------------------------------------------------------------------
try:
    if settings.DEBUG:
        import debug_toolbar
        urlpatterns += [
            url(r'^__debug__/',
                include(debug_toolbar.urls)),
        ]
except ImportError:
    pass

# -----------------------------------------------------------------------------
# Static file DEBUGGING
# -----------------------------------------------------------------------------
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import os.path

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/',
                          document_root=os.path.join(settings.MEDIA_ROOT,
                                                     'images'))
