from django.conf.urls import patterns, url

urlpatterns = patterns(
    'consumer.views',
    url(r'^$', 'startOpenID', name='startOpenID'),
    url(r'^finish/$', 'finishOpenID', name='finishOpenID'),
    url(r'^xrds/$', 'rpXRDS', name='rpXRDS'),
)
