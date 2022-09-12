"""
Views
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .models import Post, Comment
from .forms import CommentForm, ContactForm


class Home(generic.TemplateView):
    """View to display the home page"""
    template_name = "index.html"


class Reviews(generic.ListView):
    """
    View to display all album reviews in the Album Reviews page, ordered
    by creation date.
    """
    model = Post
    template_name = "blogpage.html"
    queryset = Post.objects.filter(status=1).order_by('created_date')
    paginate_by = 6


class PostDetail(generic.DetailView):
    """
    Used to display all reviews in the album reviews page, including comments
    left by logged-in users, ordered by most recently modified
    """
    model = Post
    template_name = 'review_detail.html'

    def get(self, request, slug):
        """
        To display the album review along with comments added
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-last_modified")

        return render(
            request,
            "review_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug):
        """
        This is used when a POST request is made to the view
        via the comment box, when submitting a comment.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_date")

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(self.request, 'Your commment has been added.')

        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )

# Django documentation: https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-editing/

class UpdateComment(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.UpdateView):

    """
    This view is used to allow logged in users to edit their own comments
    """
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'
    success_message = "Comment updated!"

    def form_valid(self, form):
        form.instance.name = self.request.user.username
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        """
        This validates that the user is changing their own comment
        """
        comment = self.get_object()
        return comment.name == self.request.user.username

    def get_success_url(self):
        """
        Return to review detail view when comment has
        been updated by the user
        """
        review = self.object.post
        return reverse_lazy('review_detail', kwargs={'slug': review.slug})


class DeleteComment(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):

    """
    This view is used to allow users to delete only their own comments,
    and not those of other users.
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_message = "Comment deleted!"

    def test_func(self):
        """
        This validates the comment that the user wishes to delete
        """
        comment = self.get_object()
        return comment.name == self.request.user.username

    def delete(self, request, *args, **kwargs):
        """
        Adding this to get around Django issue where success messages do not
        work with DeleteView: https://code.djangoproject.com/ticket/21926
        Suggested fix found here:
        https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """ Return to review page when comment has been deleted by user"""
        review = self.object.post
        return reverse_lazy('review_detail', kwargs={'slug': review.slug})


# Contact Form View

def contact(request):
    """
    Function based view for contact form
    """
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            subject = "PJ Fan Club Enquiry"
            body = {
                'name': form.cleaned_data['message_name'],
                'email': form.cleaned_data['message_email'],
                'message': form.cleaned_data['message_content'],
                }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'jonathanbtest@gmail.com',
                                            ['jonathanbtest@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request,
                             'Contact request submitted successfully.')
            return redirect("contact")

    form = ContactForm()
    return render(request, "contact.html", {'form': form})
