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


def createprofile(user):
    b = Broadcaster(title=user.username, user=user)
    b.save()
    return b


def base(request):
    if request.user.is_authenticated():
        if request.POST:
            stream = request.POST.get('stream')
            s = Stream.objects.get(id=stream)
            b = Broadcaster.objects.get(user=request.user)
            b.stream = s
            b.save()
            #g = GenresLog(broadcaster=b, stream=s, ip=userip)
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
        ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
        streams = get_list_or_404(Stream.objects.all())
        play = get_play(broadcaster.stream.uri)
        return render_to_response('panel.html', locals())
    else:
        return redirect('/')
        

def logout_user(request):
    logout(request)
    return redirect('/')
