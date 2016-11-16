from django.views import generic
from .models import Post, Intro, About, Contact
from django.views.generic.edit import CreateView


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


class ContactCreate(CreateView):
    model = Contact
    template_name = 'core/contact.html'
    fields = ['name', 'email', 'phone_number', 'message']
