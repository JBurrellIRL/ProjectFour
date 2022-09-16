"""
Imports for site administration page
"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Album review post management within the admin side of the site
    """

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('review')
    list_filter = ('status', 'created_date')
    search_fields = ['title', 'review', 'author']
    list_display = (
        'title', 'author', 'status', 'created_date', 'last_modified')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment management within the admin side of the site. I have left the
    'approved" column visible in the admin panel, even though this is currently
    disabled, as this may be switched back on in the future.
    """
    list_filter = ('name', 'created_date')
    search_fields = ['body', 'name']
    list_display = ('name', 'post', 'created_date', 'last_modified',
                    'approved')
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        """
        Method here is for comment approval. Although this is not currently
        switched on in the Comment model, I have left this code here in case
        we decide to switch it back on again.
        """
        queryset.update(approved=True)
