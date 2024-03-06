from django.db import models
from django.utils.text import slugify



class Tag(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)    
    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return str(self.name)
    
class TableOfContent(models.Model):
    content = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True,blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Table of Contents'

    def __str__(self):
        return str(self.content) 

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.TextField(blank = True, )
    tags = models.ManyToManyField('Tag', blank=True)
    content = models.TextField()
    publish_date = models.DateField(blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True)
    toc = models.ManyToManyField('TableOfContent', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

