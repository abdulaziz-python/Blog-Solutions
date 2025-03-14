from django.db import models
from django.urls import reverse
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    minutes_to_read = models.PositiveIntegerField(default=5)
    
    class Meta:
        ordering = ['-date_posted']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})
