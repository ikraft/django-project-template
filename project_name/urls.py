from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


# Static file handling for dev env
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()



# Autoload template tags see AUTOLOAD_TEMPLATETAGS in settings
if hasattr(settings, 'AUTOLOAD_TEMPLATETAGS'):
    from django.template.loader import add_to_builtins
    for tag in settings.AUTOLOAD_TEMPLATETAGS:
        add_to_builtins(tag)

