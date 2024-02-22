from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    """ model for user details """

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    contact = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    """ model for blog posts details """

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} by {self.author}'


class Comment(models.Model):
    """ model for details of comments on a post """

    comment = models.TextField(null=True, blank=True)
    commenter = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commented_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-commented_on']

    def __str__(self):
        return f'{self.comment} by {self.commenter}'


class Like(models.Model):
    """ model for details of likes on a post """

    liked_by = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-liked_at']

    def __str__(self):
        return f'{self.post} liked by {self.liked_by}'
