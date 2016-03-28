from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Subreddit (models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(validators=[MinLengthValidator(225)])
    creation_date = models.DateTimeField(auto_now=True)

    @property
    def current_count(self):
        """
        returns total number of posts
        """
        return self.post_set.count()

    @property
    def today_count(self):
        """
        returns posts in the last 24 hours
        """
        return timezone.now() - datetime.timedelta(hours=24) <= self.creation_date

    @property
    def daily_average(self):
        """
        gets the average count of posts over the last 7 days
        """
        this_week = timezone.now() - datetime.timedelta(days=7)
        return self.post_set.filter(creation_date__gte=this_week).count() /7

    def __str__(self):
        return self.title


class Post(models.Model):

    title = models.CharField(max_length=300)
    description = models.TextField(validators=[MinLengthValidator(225)])
    url = models.URLField(max_length=300)
    slug = models.SlugField(max_length = 100)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(User)

    @property
    def is_recent(self):
        """
        returns True / False depending on if the
        post is in the last day
        """
        return timezone.now() - datetime.timedelta(hours=24) <= self.creation_time

    def is_hot(self):
        """
        returns True / False if the post has gotten more
        than 3 comments in the past 3 hours
        """
        three_hours = timezone.now() - datetime.timedelta(hours=3)
        recent_posts = self.comment_set.filter(created_time__gte=three_hours)
        return recent_posts.count() >= 3

class Comment(models.Model):
    comment_text = models.TextField(validators=[MinLengthValidator(225)])
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)