from django.contrib import admin
from .models import Post, Intro, About, Contact


admin.site.register(Intro)
admin.site.register(About)
admin.site.register(Post)
admin.site.register(Contact)