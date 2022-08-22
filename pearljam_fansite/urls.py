from . import views
from django.urls import path

urlpatterns = [
    # path("", views.Reviews.as_view(), name='home'),
    path("", views.Home.as_view(), name='home'),
    path("album-reviews/", views.Reviews.as_view(), name='album_reviews'),
    path(
        'reviews/<slug:slug>/',
        views.PostDetail.as_view(), name='review_detail'
        ),
    path(
        'comments/<int:pk>/update_comment/',
        views.UpdateComment.as_view(), name='update_comment'
        ),

]
