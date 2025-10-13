from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField()
    thumbnail = models.ImageField(upload_to='blog/previews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_counter = models.PositiveIntegerField(default=0)
