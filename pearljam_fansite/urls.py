"""
URL Patterns for project
"""
from django.urls import path
from . import views


urlpatterns = [
    # path("", views.Reviews.as_view(), name='home'),
    path("", views.Home.as_view(), name='home'),
    path("album-reviews/", views.Reviews.as_view(), name='album_reviews'),
    path("contact.html", views.contact, name='contact'),
    path(
        'album-reviews/<slug:slug>/',
        views.PostDetail.as_view(), name='review_detail'
        ),
    path(
        'comments/<int:pk>/update_comment/',
        views.UpdateComment.as_view(), name='update_comment'
        ),
    path(
        'comments/<int:pk>/delete/',
        views.DeleteComment.as_view(), name='delete_comment'
        ),
]
