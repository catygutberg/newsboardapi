from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["author_name", "title", "content", "link", "creation_date", "upvotes"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post", "parent", "author_name", "content", "creation_date"]
