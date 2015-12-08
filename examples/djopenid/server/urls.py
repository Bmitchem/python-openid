from django.conf.urls import patterns, url

urlpatterns = patterns(
    'server.views',
    url(r'^$', 'server', name='server'),
    url(r'^xrds/$', 'idpXrds', name='idpXrds'),
    url(r'^processTrustResult/$', 'processTrustResult', name='processTrustResult'),
    url(r'^user/$', 'idPage', name='idPage'),
    url(r'^endpoint/$', 'endpoint', name='endpoint'),
    url(r'^trust/$', 'trustPage', name='trustPage'),
)
