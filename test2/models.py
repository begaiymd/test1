from django.db import models
from django.contrib.auth import get_user_model 

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='posts1', on_delete=models.CASCADE)

    def __str__(self):
        return f"Post {self.user.username} -> {self.title} "

class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments1', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments1', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment {self.user.username} -> {self.title} [{self.created_at}]"