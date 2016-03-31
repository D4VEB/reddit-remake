from reddit_app.views import SubredditsList, SubredditDetail, PostDetail, \
    AddSubreddit, UpdateSubreddit
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^subredditslist/$', SubredditsList.as_view(), name="subreddits_list"),
    url(r'^subredditdetail/(?P<id>\d+)/$', SubredditDetail.as_view(), name="subreddit_detail"),
    url(r'^postdetail/(?P<id>\d+)/$', PostDetail.as_view(), name="post_detail"),
    url(r'^addsubreddit/$', AddSubreddit.as_view(), name="add_subreddit"),
    url(r'^updatesubreddit/(?P<id>\d+)/$', UpdateSubreddit.as_view(), name="update_subreddit"),
]