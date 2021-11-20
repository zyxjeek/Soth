from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    topic = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'BlogPosts'

    def __str__(self):
        return self.topic[:10] + '...'
