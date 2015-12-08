from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'djopenid.views.index'),
    url(r'^consumer/', include('djopenid.consumer.urls', namespace='consumer')),
    url(r'^server/', include('djopenid.server.urls', namespace='server')),
)
