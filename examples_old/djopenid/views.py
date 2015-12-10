from django.core.urlresolvers import reverse
from django.shortcuts import render

def index(request):
    consumer_url = reverse('djopenid.consumer.views.startOpenID')
    server_url = reverse('djopenid.server.views.server')

    return render(request, 'djopenid/index.html', {'consumer_url':consumer_url, 'server_url':server_url})

