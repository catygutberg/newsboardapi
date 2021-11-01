from django.db import models


class Post(models.Model):
    author_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()
    link = models.URLField(max_length=100, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True)
    author_name = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
