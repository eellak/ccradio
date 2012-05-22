# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.conf.urls.defaults import *
from datetime import date
from ccradio.panel.models import Broadcaster, BroadcasterForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail


def get_play(stream):
    import urllib2
    from BeautifulSoup import BeautifulSoup
    try:
        html = urllib2.urlopen(settings.ICECAST_URL).read()
    except:
        play = settings.RADIO_URL
        return play
    soup = BeautifulSoup(html)
    
    tdtags = soup.findAll('td', { "class" : "streamdata" })
    live = stream[4:5]
    tag = (int(live) * 11) - 1
    try:
        play = tdtags[tag].contents[0]
    except:
        play = settings.RADIO_URL
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


def register(request):
    if request.user.is_authenticated():
        return redirect('/panel/')
    if request.POST:
        form = BroadcasterForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            send_mail('[ccradio] Registration', 'title: '+f.title+'\nurl: '+f.url+'\nabout: '+f.about+'\ncategory: '+str(f.category_id), f.email,
    ['nikos@autoverse.net'], fail_silently=False)
            return redirect('/thanks/')
    else:
        form = BroadcasterForm()
    return render_to_response('register.html', locals())
    
    
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
            play = get_play(broadcaster.stream)
        else:
            play = get_play('0')
        return render_to_response('play.html', {'play': play})
    else:
        return redirect('/')
