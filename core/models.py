from __future__ import unicode_literals
from django.utils.encoding import force_bytes
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


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


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=15)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
