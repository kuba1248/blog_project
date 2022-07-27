from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post ({self.author.username}) => {self.title}"


class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment ({self.author.username}) => {self.post.title} [{self.created_at}]"


class Like(models.Model):
    author = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Like ({self.author.username}) => {self.post.title}"