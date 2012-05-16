# -*- coding: utf-8 -*-
from django.db import models
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
    url = models.URLField(max_length=150, blank=True)
    about = models.TextField()
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    stream = models.ForeignKey(Stream)
    user = models.ForeignKey(User, unique=True)
    
    def __unicode__(self):
	    return self.title

    class Meta:
        ordering = ["title", "category__name"]


class GenresLog(models.Model):
    date = models.DateField()
    broadcaster = models.ForeignKey(Broadcaster)
    stream = models.ForeignKey(Stream)
