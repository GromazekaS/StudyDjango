from .models import Post
from django.views.generic import DetailView, DeleteView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django import forms
from django.core.mail import send_mail


class PostListView(ListView):
    model = Post
    template_name = 'blog_example_page'
    context_object_name = 'post'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_example_page'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    fields = ['title','text', 'thumbnail']
    template_name = 'blog_example_page'
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','text', 'thumbnail', 'is_published']
    template_name = 'blog_example_page'
    success_url = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_example_page'
    success_url = reverse_lazy('post_list')


from django.shortcuts import render

# Create your views here.
