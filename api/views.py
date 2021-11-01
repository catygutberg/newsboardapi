from django.db.models import F
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostListView(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        return Response(PostSerializer(instance=queryset, many=True).data)


class PostView(APIView):
    def get(self, request):
        queryset = Post.objects.filter(id=request.GET.get("id"))
        return Response(PostSerializer(instance=queryset, many=True).data)

    def post(self, request):
        post = Post(
            title=request.data["title"],
            content=request.data["content"],
            author_name=request.data["author_name"],
        )
        post.clean()
        post.save()
        post.link = f"/post?id={post.id}"
        post.save()
        return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)

    def put(self, request):
        post = Post.objects.get(id=request.GET.get("id"))
        post.title = request.data["title"]
        post.content = request.data["content"]
        post.clean()
        post.save()
        return Response(PostSerializer(post).data)

    def delete(self, request):
        Post.objects.get(id=request.GET.get("id")).delete()
        return Response()


class UpvoteView(APIView):
    def put(self, request):
        queryset = Post.objects.filter(id=request.GET.get("id"))
        queryset.update(upvotes=F("upvotes") + 1)
        return Response()


class CommentListView(APIView):
    def get(self, request):
        queryset = Comment.objects.filter(post_id=request.GET.get("post_id"))
        return Response(CommentSerializer(instance=queryset, many=True).data)


class CommentView(APIView):
    def get(self, request):
        queryset = Comment.objects.filter(id=request.GET.get("id"))
        return Response(CommentSerializer(instance=queryset, many=True).data)

    def post(self, request):
        comment = Comment(
            author_name=request.data["author_name"],
            content=request.data["content"],
            post=Post.objects.get(id=request.data["post"]),
            parent=Comment.objects.get(id=request.data["parent"])
            if "parent" in request.data.keys() and request.data["parent"] != ""
            else None,
        )
        comment.clean()
        comment.save()
        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)

    def put(self, request):
        comment = Comment.objects.get(id=request.GET.get("id"))
        comment.content = request.data["content"]
        comment.clean()
        comment.save()
        return Response(CommentSerializer(comment).data)

    def delete(self, request):
        Comment.objects.get(id=request.GET.get("id")).delete()
        return Response()
