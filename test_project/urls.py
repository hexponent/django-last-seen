from django.conf.urls import url
from last_seen.models import clear_interval
from django.shortcuts import redirect

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


def clear(request):
    """ Testing view to force clear interval of user"""
    clear_interval(request.user)
    return redirect("/admin")


urlpatterns = [
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^test_project/', include('test_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
    url(r'^clear/', clear),
]
