from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from core.forms import ContactForm
from .models import Post, Intro, About


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'all_intros'

    def get_queryset(self):
        return Intro.objects.all()


class BlogView(generic.ListView):
    template_name = 'core/blog.html'
    context_object_name = 'all_posts'
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.all()


class ReadMoreView(generic.DeleteView):
    model = Post
    template_name = 'core/readmore.html'


class AboutView(generic.ListView):
    template_name = 'core/about.html'
    context_object_name = 'all_abouts'

    def get_queryset(self):
        return About.objects.all()


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Assunto']
            from_email = form.cleaned_data['Email']
            message = form.cleaned_data['Messagem']
            fullMessage = "Email do cliente: " + from_email + '\n' '\n' + message
            try:
                send_mail(subject, fullMessage, from_email, ['docealho@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    return render(request, "core/contact.html", {'form': form})