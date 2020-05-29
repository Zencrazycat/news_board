from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from news_posts.models import Post, Comment
from news_posts.api.serializers import PostSerializer, CommentSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostsView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination


class PostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self, *args, **kwargs):
        super().get_queryset()
        self.queryset = Comment.objects.filter(post=self.kwargs['pk'])
        return self.queryset


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination


class CommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        super().get_queryset()
        self.queryset = Comment.objects.filter(id=self.kwargs['pk'])
        return self.queryset


class UpvoteView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        object = Post.objects.get(id=self.kwargs['pk'])
        object.upvotes += 1
        object.save()
        return super().get_object()
