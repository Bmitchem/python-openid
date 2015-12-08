from django.shortcuts import render

from examples.djopenid import util


def index(request):
    consumer_url = util.getViewURL(
        request, 'djopenid.consumer.views.startOpenID')
    server_url = util.getViewURL(request, 'djopenid.server.views.server')

    return render(
        request,
        'index.html',
        {'consumer_url':consumer_url, 'server_url':server_url})

