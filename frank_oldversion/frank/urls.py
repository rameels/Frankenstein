from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^frank/', include('frankapp.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.search, name='search')
    url(r'^$', views.results, name='results')
)
