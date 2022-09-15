"""
Models imports
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Tuple for blog post status
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model for album review
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    review = models.TextField()
    excerpt = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    album_release_date = models.TextField(blank=True)
    album_producer = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="album_reviews"
    )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        To display the created reviews in order by created date.
        """
        ordering = ['-created_date']

    def __str__(self):
        """
        Django method to return a string rather than an object
        """
        return self.title


# Commenting model

class Comment(models.Model):
    """
    Comment model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)

    class Meta:
        """
        To display comments in order by most recently modified.
        """
        ordering = ['last_modified']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
