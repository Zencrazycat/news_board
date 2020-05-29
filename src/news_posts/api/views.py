from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from news_posts.api.serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostsView(generics.ListCreateAPIView):
    pass


class PostView(generics.RetrieveUpdateDestroyAPIView):
    pass


class CommentsView(generics.ListCreateAPIView):
    pass


class CommentView(generics.RetrieveUpdateDestroyAPIView):
    pass
