from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from reddit_app.forms import SubredditForm
from reddit_app.models import Subreddit, Post
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.utils import timezone


class SubredditList(ListView):
    model = Subreddit
    queryset = Subreddit.objects.order_by("-creation_date")
    paginate_by = 5


class SubredditDetail(DetailView):
    model = Subreddit
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = self.object.post_set.all().order_by("-creation_time")[:20]
        return context

# Note to self. Need to come update this to a generic view


class PostDetail(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comment_set.all()
        return context

class AddSubreddit(LoginRequiredMixin, CreateView):
    model = Subreddit
    form_class = SubredditForm
    success_url = reverse_lazy("subreddit_list")
    template_name_suffix = "_add"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateSubreddit(LoginRequiredMixin, UpdateView):
    model = Subreddit
    form_class = SubredditForm
    pk_url_kwarg = "id"
    template_name_suffix = "_update"

    def get_success_url(self):
       return reverse("subreddit_detail", args=(self.object.id,))