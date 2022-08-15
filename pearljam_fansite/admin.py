from django.contrib import admin
from .models import AlbumReview, Comment
from django_summernote.admin import SummernoteModelAdmin


# Album review admin model 
@admin.register(AlbumReview)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('review')
    list_filter = ('status', 'created_date')
    search_fields = ['title', 'review', 'author']
    list_display = ('title', 'author', 'status', 'created_date', 'last_modified')

 
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('name', 'approved', 'created_date')
    search_fields = ['body', 'name']
    list_display = ('name', 'body', 'post', 'created_date', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)