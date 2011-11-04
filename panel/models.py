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


class BroadcastUser(models.Model):
    GENRES = (
        ('1', 'Jazz'),
    	('2', 'Rock'),
    	('3', 'Electronic'),
	    ('4', 'Pop'),
    	('5', 'Alternative'),
	    ('6', 'Jazz+Rock'),
	    ('7', 'Jazz+Electronic'),
	    ('8', 'Rock+Alternative'),
	    ('9', 'Pop+Electronic'),
	    ('10', 'Everything'),
    )
    url = models.URLField(max_length=150, blank=True)
    email = models.CharField(max_length=150, blank=True)
    about = models.TextField()
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, unique=True)
    title = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    stream = models.CharField(max_length="1", choices=GENRES)
    
    def __unicode__(self):
	    return self.name

    class Meta:
	    ordering = ["title", "category"]
