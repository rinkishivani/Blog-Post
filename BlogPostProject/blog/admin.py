from django.contrib import admin
from .models import User, Post, Comment, Like


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('contact', 'created_at')


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_at')


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('comment', 'post', 'commenter')


@admin.register(Like)
class Like(admin.ModelAdmin):
    list_display = ('liked_at', 'liked_at')
