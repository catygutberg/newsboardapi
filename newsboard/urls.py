from django.contrib import admin
from django.urls import path

from api.views import PostView, PostListView, UpvoteView, CommentView, CommentListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/posts/", PostListView.as_view()),
    path("api/post/", PostView.as_view()),
    path("api/post/upvote/", UpvoteView.as_view()),
    path("api/comments/", CommentListView.as_view()),
    path("api/comment/", CommentView.as_view()),
]
