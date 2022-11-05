from django.shortcuts import render
# added

from .models import Post
from django.views import generic

# Create your views here.


class BlogView(generic.DetailView):  # DetailView render html by getting data from model
    model = Post
    template_name = 'blog.html'


# TemplateView render html without getting data from model
class AboutView(generic.TemplateView):
    template_name = 'about.html'


class PostList(generic.ListView):  # ListView render html by getting data from multiple post
    queryset = Post.objects.filter(status=1).order_by('date_created')
    template_name = 'index.html'
