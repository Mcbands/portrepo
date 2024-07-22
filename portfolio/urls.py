from django.urls import path
from portfolio.views import GetPostBySlug

urlpatterns = [
    path("<slug:slug>/", GetPostBySlug.as_view(), name="post_by_slug"),
]
