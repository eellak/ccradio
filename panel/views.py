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


def base(request):
    if request.user.is_authenticated():
        if request.POST:
            stream = request.POST.get('stream')
            s = Stream.objects.get(id=stream)
            b = Broadcaster.objects.get(user=request.user)
            b.stream = s
            b.save()
            """
            stime = strftime("%H:%M:%S")
            GenresLog.date = stime
            GenresLog.broadcaster = b
            GenresLog.stream = s
            GenresLog.save()
            """
            
        broadcaster = get_object_or_404(Broadcaster.objects.filter(user=request.user))
        ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
        streams = get_list_or_404(Stream.objects.all())
        play = get_play(broadcaster.stream.uri)
        return render_to_response('panel.html', locals())
    else:
        return redirect('/')
        

def logout_user(request):
    logout(request)
    return redirect('/')
