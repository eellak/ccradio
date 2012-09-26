# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.conf.urls.defaults import *
from datetime import date
from ccradio.panel.models import Broadcaster
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail

ICECAST_URL = settings.ICECAST_URL
RADIO_URL = settings.RADIO_URL
LOGS_URL = settings.LOGS_URL
STREAM_URL = settings.STREAM_URL


def get_play(stream):
    import urllib2
    from BeautifulSoup import BeautifulSoup
    try:
        html = urllib2.urlopen(ICECAST_URL).read()
    except:
        play = RADIO_URL
        return play
    soup = BeautifulSoup(html)
    
    tdtags = soup.findAll('td', { "class" : "streamdata" })
    live = stream[4:5]
    print live
    tag = ((int(live) + 1) * 11) - 1
    try:
        play = tdtags[tag].contents[0]
        play = play.replace ("_", " ")
        play = play.replace ("-", " - ")
    except:
        play = RADIO_URL
    return play


def base(request):
    if request.user.is_authenticated():
        return redirect('/panel/')
    play = get_play('live0')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/panel/')
            else:
                authstate = "Ο λογαριασμός σας έχει απενεργοποιηθεί!"
        else:
            authstate = "Τα στοιχεία που εισάγατε δεν είναι σωστά!"
    return render_to_response('base.html', locals())
    

def about(request):
    return render_to_response('about.html', locals())
    
    
def tos(request):
    return render_to_response('tos.html', locals())


def thanks(request):
    if request.user.is_authenticated():
        return redirect('/panel/')
    return render_to_response('thanks.html', locals())


def play(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            broadcaster = get_object_or_404(Broadcaster.objects.filter(user=request.user))
            play = get_play(broadcaster.stream.uri)
        else:
            play = get_play('live0')
        return render_to_response('play.html', {'play': play})
    else:
        return redirect('/')
