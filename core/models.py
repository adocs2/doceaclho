from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    introduction = models.CharField(max_length=250)
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.FileField()

    def __str__(self):
        return self.title


class Intro(models.Model):
    title = models.CharField(max_length=150)
    text = RichTextField()

    def __str__(self):
        return self.title


class About(models.Model):
    photo = models.FileField()
    text = RichTextField()
