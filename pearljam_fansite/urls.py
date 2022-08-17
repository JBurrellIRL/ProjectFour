from . import views
from django.urls import path

urlpatterns = [
    # path("", views.Reviews.as_view(), name='home'),
    path("", views.Home.as_view(), name='home'),
    path("album-reviews/", views.Reviews.as_view(), name='album_reviews'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='review_detail'),

]
