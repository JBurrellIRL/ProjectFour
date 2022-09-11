"""
URL configuration
"""

from django.contrib import admin
from django.urls import path, include
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp

admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("pearljam_fansite.urls"), name="blog_urls"),
    path('accounts/', include('allauth.urls')),

]
