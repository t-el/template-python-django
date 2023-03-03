from django.db import models
import uuid
# Create your models here.

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('app:posts_by_category', args=[self.slug])
        
from ckeditor_uploader.fields import RichTextUploadingField 
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='blog_posts')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        uid = str(uuid.uuid4())[:8]
        self.slug = uid+slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('app:post_detail', args=[self.slug])




