import datetime
from django.utils import timezone
from django.test import TestCase
from reddit_app.models import Subreddit, Post, Comment
from django.contrib.auth.models import User


class SubredditTests(TestCase):

    text_for_testing = 'This is only a test.' * 15

    def setUp (self):
        self.user = User.objects.create_user(username='testuser', email='testuser@test.com', password='securepassword')
        self.subreddit = Subreddit.objects.create(title="subreddit1", descriptions = 'I created this for testing')
        self.firstpost = Post.objects.create(title="test post1", description=self.text_for_testing, user=self.user, subreddit=self.subreddit)
        self.secondpost = Post.objects.create(title="test post2", description=self.text_for_testing, user=self.user, subreddit=self.subreddit)

    def test_current_count(self):
        self.assertEqual(self.subreddit.post_count, 2, "Incorrect count")

    def test_today_count(self):
        self.secondpost.creation_date = timezone.now() - datetime.timedelta(days=2)
        self.secondpost.save()
        self.assertEqual(self.subreddit.today_count, 1, "Incorrect count")


class PostTests(TestCase):
    text_for_testing = 'This is only a test.' * 15

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@test.com', password='securepassword')
        self.subreddit = Subreddit.objects.create(title="subreddit1", descriptions='I created this for testing')
        self.firstpost = Post.objects.create(title="test post1", description=self.text_for_testing, user=self.user, subreddit=self.subreddit)
        self.secondpost = Post.objects.create(title="test post2", description=self.text_for_testing, user=self.user, subreddit=self.subreddit)
        self.firstcomment = Comment.objects.create(1)
        self.secondcomment = Comment.objects.create(2)
        self.thirdcomment = Comment.objects.create(3)

    def test_is_recent(self):
        self.firstpost.creation_date = timezone.now() - datetime.timedelta(hours=12)
        self.secondpost.save()
        self.assertEqual(self.secondpost, True, "Wrong. The post IS recent.")

    def test_is_hot(self):
        first_comment = timezone.now() - datetime.timedelta(years=1)
        self.firstcomment.created_time=first_comment
        self.firstcomment.save()
        self.assertFalse(self.firstpost.is_hot(), msg = "The post is NOT hot.")


