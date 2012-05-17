# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="κατηγορία")
    slug = models.SlugField(help_text="<b>συμπληρώνεται αυτόματα!</b>")

    def __unicode__(self):
	    return self.name

    class Meta:
	    ordering = ["name"]
	    verbose_name_plural = "Categories"


class Stream(models.Model):
    name = models.CharField(max_length=50, verbose_name="κατηγορία")
    uri = models.CharField(max_length=100)

    def __unicode__(self):
	    return self.name

    class Meta:
	    ordering = ["uri"]


class Broadcaster(models.Model):
    title = models.CharField(max_length=120, verbose_name="Όνομα")
    url = models.URLField(max_length=150, blank=True, verbose_name="Website")
    category = models.ForeignKey(Category, verbose_name="Δραστηριότητα")
    about = models.TextField(verbose_name="Περιγραφή")
    active = models.BooleanField(default=False)
    stream = models.ForeignKey(Stream, default=1)
    user = models.ForeignKey(User, unique=True, blank=True)
    
    def __unicode__(self):
	    return self.title

    class Meta:
        ordering = ["title", "category__name"]


class GenresLog(models.Model):
    date = models.DateField()
    broadcaster = models.ForeignKey(Broadcaster)
    stream = models.ForeignKey(Stream)
    ip = models.CharField(max_length=15)
    

class BroadcasterForm(ModelForm):
    class Meta:
        model = Broadcaster
        exclude = ('active', 'stream', 'user')
