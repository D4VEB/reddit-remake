from django.shortcuts import render, get_object_or_404
# from django.db.models import Count
from django.views.generic import View

from reddit_app.forms import NewSubredditForm
from reddit_app.models import Subreddit, Post


class SubredditsList(View):
    def get(self, request):
        subreddits = Subreddit.objects.all()

        return render(request, "reddit_app/subreddit_list.html",
                      {'subreddits': subreddits})

class SubredditDetail(View):

    def get(self, request, id):
        subreddit = get_object_or_404(Subreddit, pk=id)
        posts = subreddit.post_set.order_by("-creation_date")[:20]
        return render(request, "reddit_app/subreddit_details.html",
                      {'subreddit': subreddit, "posts": posts})


class PostDetail(View):
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        comments = post.comment_set.order_by("-creation_date")
        return render(request, "reddit_app/post_details.html", {"post": post,"comments": comments})

class AddSubreddit(View):
    def get(self, request):
        form = NewSubredditForm()
        return render(request, "reddit_app/new_subreddit.html", {"form":form})