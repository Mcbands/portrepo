from django.urls import path
from blog_app.views import (
    PostsByCategory,
    GetPostBySlug,
    SearchCategory,
)

urlpatterns = [
    path("category/<int:id>/", PostsByCategory.as_view(), name="post_by_category"),  # Fixed URL pattern
    path("post/<slug:slug>/", GetPostBySlug.as_view(), name="post_by_slug"),  # Fixed URL pattern
    path("search/", SearchCategory.as_view(), name="search_category"),
]
