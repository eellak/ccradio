# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.conf.urls.defaults import *
from django.contrib.auth.models import User
from datetime import date
from ccradio.panel.models import Broadcaster, Category
from ccradio.views import get_play


def base(request):
    if request.user.is_authenticated():
        broadcaster = get_object_or_404(Broadcaster.objects.filter(user=request.user))
        play = get_play(broadcaster.stream)
        return render_to_response('panel.html', locals())
    else:
        return redirect('/')
