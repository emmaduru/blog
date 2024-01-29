from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = "post"

class PostCreateView(CreateView):
    model = Post
    template_name = "create.html"
    fields = ("title", "description",)

class PostUpdateView(UpdateView):
    model = Post
    template_name = "edit.html"
    fields = ("title", "description",)

class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("home")
