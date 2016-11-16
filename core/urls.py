from django.conf.urls import url
from . import views
from .models import Contact

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about$', views.AboutView.as_view(), name='about'),
    url(r'^blog$', views.BlogView.as_view(), name='blog'),
    url(r'^readmore(?P<pk>[0-9]+)$', views.ReadMoreView.as_view(), name='readmore'),
    url(r'^contact/add$', views.ContactCreate.as_view(model=Contact, success_url="../"), name='contact-add'),
]
