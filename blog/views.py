from .models import Post
from django.views.generic import DetailView, DeleteView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django import forms
from django.core.mail import send_mail


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Возвращаем только опубликованные посты
        return Post.objects.filter(is_published=True)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/full_post.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # Получаем объект поста
        self.object = self.get_object()

        # Увеличиваем счетчик просмотров
        self.object.views_counter += 1
        self.object.save()

        # Продолжаем стандартную обработку запроса
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



class PostCreateView(CreateView):
    model = Post
    fields = ['title','text', 'thumbnail']
    template_name = 'blog/new_post.html'
    success_url = reverse_lazy('posts_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','text', 'thumbnail', 'is_published']
    template_name = 'blog/post_edit.html'

    def get_success_url(self):
        # После успешного обновления объекта (статьи) перенаправляем на его детальную страницу
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')


from django.shortcuts import render

# Create your views here.
