from rest_framework import generics
from blog.models import Post
from blog.serializers import PostListSerializer, PostDetailSerializer


class PostList(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
