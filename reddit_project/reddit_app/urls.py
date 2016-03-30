from reddit_app.views import SubredditsList, SubredditDetail, PostDetail
from django.conf.urls import url

urlpatterns = [
    url(r'^subbreditslist/$', SubredditsList.as_view(), name="subreddits_list"),
    url(r'^subredditdetail(?P<id>\d+)/$', SubredditDetail.as_view(), name="subreddit_detail"),
    url(r'^postdetail/$', PostDetail.as_view(), name="post_detail"),
    #url(r'^addsubreddit/$', AddSubreddit.as_view(), name="add_subbreddit"),

]