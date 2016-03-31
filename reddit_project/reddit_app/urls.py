from reddit_app.views import SubredditList, SubredditDetail, PostDetail, \
    AddSubreddit, UpdateSubreddit
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^subreddit_list/$', SubredditList.as_view(), name="subreddit_list"),
    url(r'^subreddit_detail/(?P<id>\d+)/$', SubredditDetail.as_view(), name="subreddit_detail"),
    url(r'^post_detail/(?P<id>\d+)/$', PostDetail.as_view(), name="post_detail"),
    url(r'^subreddit_add/$', AddSubreddit.as_view(), name="subreddit_add"),
    url(r'^subreddit_update/(?P<id>\d+)/$', UpdateSubreddit.as_view(), name="subreddit_update"),
]