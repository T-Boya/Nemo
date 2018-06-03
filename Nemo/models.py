from django.db import models
from django import forms
from django.template.defaultfilters import slugify
from django.shortcuts import redirect

class Room(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(default='', blank=True)
    admin = models.CharField(max_length=45)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Message(models.Model):
    message = models.CharField(max_length=1000)
    poster = models.CharField(max_length=10)
    room = models.ForeignKey(Room)
