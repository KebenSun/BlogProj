from django.db import models


class Comment(models.Model):
    """评论模型"""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    #url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

class Like(models.Model):
    """赞"""
    comment = models.ForeignKey('comments.Comment', on_delete=models.CASCADE)
    ip = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)

class Tread(models.Model):
    """踩"""
    comment = models.ForeignKey('comments.Comment', on_delete=models.CASCADE)
    ip = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
