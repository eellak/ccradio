# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.conf.urls.defaults import *
from datetime import date
from ccradio.panel.models import Broadcaster


def get_play(stream):
    import urllib2
    from BeautifulSoup import BeautifulSoup
    try:
        html = urllib2.urlopen("http://stream.creativecommons.gr:8000/status.xsl").read()
    except:
        play = "radio.creativecommons.gr"
    soup = BeautifulSoup(html)
    #livetags = soup.findAll('h3')
    
    tdtags = soup.findAll('td', { "class" : "streamdata" })
    tag = (int(stream) * 11) - 1
    try:
        play = tdtags[tag].contents[0]
    except:
        play = "radio.creativecommons.gr"
    return play
        

def base(request):
    if request.user.is_authenticated():
        return redirect('/panel/')
    else:
        play = get_play('10')
    return render_to_response('base.html', locals())


def play(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            broadcaster = get_object_or_404(Broadcaster.objects.filter(user=request.user))
            play = get_play(broadcaster.stream)
        else:
            play = get_play('10')
        return render_to_response('play.html', {'play': play})
    else:
        return redirect('/')
