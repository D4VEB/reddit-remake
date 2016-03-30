from django.shortcuts import render, get_object_or_404, redirect
# from django.db.models import Count
from django.views.generic import View

from reddit_app.forms import SubredditForm
from reddit_app.models import Subreddit, Post
from django.core.urlresolvers import reverse


class SubredditsList(View):

    def get(self, request):
        subreddits = Subreddit.objects.all()

        return render(request, "reddit_app/subreddits_list.html",
                      {'subreddits': subreddits})

class SubredditDetail(View):

    def get(self, request, id):
        subreddit = get_object_or_404(Subreddit, pk=id)
        posts = subreddit.post_set.order_by("-creation_time")[:20]
        return render(request, "reddit_app/subreddit_detail.html",
                      {'subreddit': subreddit, "posts": posts})


class PostDetail(View):

    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        comments = post.comment_set.order_by("-created_time")
        return render(request, "reddit_app/post_detail.html", {"post": post,"comments": comments})


class AddSubreddit(View):

    def get(self, request):
        form = SubredditForm()
        return render(request, "reddit_app/add_subreddit.html", {"form":form})


class UpdateSubreddit(View):

    def get(self, request, id):
        subreddit = get_object_or_404(Subreddit, pk=id)

        form = SubredditForm(instance=subreddit)

        return render(request, "reddit_app/update_subreddit.html",
                      {"form": form, "subreddit": subreddit})

    def post(self, request, id):
        subreddit = get_object_or_404(Subreddit, pk=id)

        form = SubredditForm(data=request.POST, instance=subreddit)

        if form.is_valid():
            form.save()

            return redirect(reverse("subreddits_list"))
        return render(request, "reddit_app/update_subreddit.html",
                      {"form": form, "subreddit": subreddit})