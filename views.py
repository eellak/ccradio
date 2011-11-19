# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.conf.urls.defaults import *
from datetime import date
from ccradio.panel.models import Broadcaster


def get_play(stream):
    import urllib2
    from BeautifulSoup import BeautifulSoup
    html = urllib2.urlopen("http://radio.creativecommons.gr:8000/status.xsl").read()
    
    soup = BeautifulSoup(html)
    #livetags = soup.findAll('h3')
    
    tdtags = soup.findAll('td', { "class" : "streamdata" })
    try:
        play = tdtags[int(stream)-1].contents[0]
    except:
        play = "radio.creativecommons.gr"
    return play
        

def base(request):
    if request.user.is_authenticated():
        isonline = True
        broadcaster = get_object_or_404(Broadcaster.objects.filter(user=request.user))
        play = get_play(broadcaster.stream)
    else:
        play = get_play('10')
        isonline = False
    return render_to_response('base.html', locals())


def play(request):
    if request.is_ajax():
        play = get_play()
        return render_to_response('play.html', {'play': play})
    else:
        return redirect('/')
