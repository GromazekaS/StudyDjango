from .models import Post
from django.views.generic import DetailView, DeleteView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django import forms
from django.core.mail import send_mail


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/full_post.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    fields = ['title','text', 'thumbnail']
    template_name = 'blog/new_post.html'
    success_url = reverse_lazy('posts_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','text', 'thumbnail', 'is_published']
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('posts_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')


from django.shortcuts import render

# Create your views here.
