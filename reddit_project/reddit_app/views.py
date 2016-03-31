from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from reddit_app.forms import SubredditForm
from reddit_app.models import Subreddit, Post
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView

from django.utils import timezone


class SubredditsList(ListView):
    model = Subreddit
    queryset = Subreddit.objects.order_by("-creation_date")
    paginate_by = 5


class SubredditDetail(DetailView):
    model = Subreddit
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time_run"] = timezone.now()
        return context

# Note to self. Need to come update this to a generic view
class PostDetail(View):
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        comments = post.comment_set.order_by("-created_time")
        return render(request, "reddit_app/post_detail.html",
                      {"post": post, "comments": comments})


class AddSubreddit(LoginRequiredMixin, CreateView):
    model = Subreddit
    form_class = SubredditForm
    success_url = reverse_lazy("subreddits_list")
    template_name_suffix = "_create"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateSubreddit(LoginRequiredMixin, UpdateView):
    model = Subreddit
    form_class = SubredditForm
    template_name = "reddit_app/update_subreddit.html"

    def get_success_url(self):
       return reverse("subreddit_detail", args=(self.object.id,))