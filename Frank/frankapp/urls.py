from django.conf.urls import patterns, url


from frankapp import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
