from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class Home(generic.TemplateView):
    """View to display the home page"""
    template_name = "index.html"


class Reviews(generic.ListView):
    """
    View to display all album reviews in the Album Reviews page
    """
    model = Post
    template_name = "blogpage.html"
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    paginate_by = 9


# class ReviewsDetail(generic, DetailView):
#     """
#     View to display the full album review plus comments left by logged-in users
#     """
#     def get(self, request, slug):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by("-created_on")

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'review_detail.html'