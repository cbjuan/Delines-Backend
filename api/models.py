# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm, Textarea
from django import forms

# Create your models here.
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe


class Position (models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=7)
    longitude = models.DecimalField(max_digits=12, decimal_places=7)
    elevation = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Route (models.Model):
    id = models.AutoField(primary_key=True)
    transport = models.CharField(max_length=255, null=True, blank=True)
    position = models.ManyToManyField(Position, null=True, blank=True)

class User (models.Model):
    id = models.AutoField(primary_key=True)
    routes = models.ManyToManyField(Route, null=True, blank=True)