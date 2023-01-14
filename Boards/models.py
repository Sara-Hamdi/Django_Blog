from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    describtion = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Posts.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Posts.objects.filter(topic__board=self).order_by('-created_date').first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(
        Board, related_name="topics", on_delete=models.CASCADE)
    creator = models.ForeignKey(
        User, related_name="topics", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.subject


class Posts(models.Model):
    comment = models.TextField(max_length=4000)
    topic = models.ForeignKey(
        Topic, related_name="posts", on_delete=models.CASCADE)
    creator = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        truncated_comment = Truncator(self.comment)
        return truncated_comment.chars(30)
