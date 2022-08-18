from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post
from .forms import CommentForm


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


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'review_detail.html'

    def get(self, request, slug,):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_date")

        return render(
            request,
            "review_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_date")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            response = redirect('/album-reviews')
            return response
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm()
            },
        )