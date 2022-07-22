from rest_framework import generics
from blog.models import Post
from blog.serializers import PostListSerializer


class PostList(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
