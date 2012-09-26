# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpRequest
from django.conf.urls.defaults import *
from django.contrib.auth.models import User
from datetime import date
from ccradio.panel.models import Broadcaster, Category, Stream, GenresLog
from ccradio.views import get_play
from django.contrib.auth import logout
from django.db import IntegrityError
from time import strftime
from django.conf import settings

ICECAST_URL = settings.ICECAST_URL
RADIO_URL = settings.RADIO_URL
LOGS_URL = settings.LOGS_URL


def createprofile(user):
    b = Broadcaster(title=user.username, user=user)
    b.save()
    return b
    
    
def get_userip(request):
    ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
    if ip:
        ip = ip.split(", ")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", "")
    return ip



def base(request):
    if request.user.is_authenticated():
        userip = get_userip(request)
        if request.POST:
            stream = request.POST.get('stream')
            s = Stream.objects.get(id=stream)
            b = Broadcaster.objects.get(user=request.user)
            b.stream = s
            b.save()
            g = GenresLog(broadcaster=b, stream=s, ip=userip)
            g.save()
            """
            stime = strftime("%H:%M:%S")
            GenresLog.date = stime
            GenresLog.broadcaster = b
            GenresLog.stream = s
            GenresLog.save()
            """
        try:
            broadcaster = Broadcaster.objects.get(user=request.user)
        except:
            broadcaster = createprofile(request.user)
        streams = get_list_or_404(Stream.objects.all())
        play = get_play(broadcaster.stream.uri)
        return render_to_response('panel.html', locals())
    else:
        return redirect('/')
        

def logout_user(request):
    logout(request)
    return redirect('/')
