from reddit_app.models import Subreddit
from django import forms

class NewSubredditForm(forms.ModelForm):

    class Meta:
        model = Subreddit
        fields = ("title", "description")


