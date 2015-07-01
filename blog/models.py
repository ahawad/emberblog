from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=255,unique=True)
    post_create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog_Post'
        verbose_name_plural = 'Blog_Posts'
        ordering=['-post_create_date']
