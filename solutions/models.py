from django.db import models
from django.urls import reverse
from django.utils import timezone

class QuestionType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class Solution(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='solutions')
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE, related_name='solutions')
    description = models.TextField()
    solution_code = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    external_link = models.URLField(blank=True)
    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('solution-detail', kwargs={'slug': self.slug})
