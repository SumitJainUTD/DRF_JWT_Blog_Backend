from django.db import models
from django.utils import timezone
from ..users.models import CustomUser as User


class Post(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)