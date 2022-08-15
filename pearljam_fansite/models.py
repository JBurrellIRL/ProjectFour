from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Tuple for blog post status
STATUS = ((0, "Draft"), (1, "Published"))


# Album review model
class AlbumReview(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    review = models.TextField()
    excerpt = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="album_reviews"
    )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


# Commenting model 

class Comment(models.Model):
    post = models.ForeignKey(AlbumReview, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"