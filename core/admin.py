from django.contrib import admin

from .models import Post, Intro, About

admin.site.register(Intro)
admin.site.register(About)
admin.site.register(Post)
