from django.contrib import admin
from reddit_app.models import Subreddit, Post, Comment

# Register your models here.

@admin.register(Subreddit)
class SubredditAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'creation_date')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'url', 'slug', 'creation_time', 'modification_time')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_text', 'user', 'post', 'created_time', 'modified_time')
