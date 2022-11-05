from email.policy import default
from pickle import TRUE
from telnetlib import STATUS
from unittest.util import _MAX_LENGTH
from django.db import models

# added
from django.contrib.auth.models import User
from django.urls import reverse


STATUS = ((0, 'Draft'), (1, 'Publish'))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=TRUE)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_view", kwargs={"slug": self.slug})

# added
