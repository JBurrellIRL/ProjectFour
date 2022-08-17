from . import views
from django.urls import path

urlpatterns = [
    # path("", views.Reviews.as_view(), name='home'),
    path("", views.Home.as_view(), name='home'),
    path("album-reviews/", views.Reviews.as_view(), name='album_reviews'),

]
