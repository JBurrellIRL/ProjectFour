from django.contrib import admin
from .models import AlbumReview
from django_summernote.admin import SummernoteModelAdmin


@admin.register(AlbumReview)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('review',)
