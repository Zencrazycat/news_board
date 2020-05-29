from rest_framework import serializers

from news_posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'link',
            'creation_date',
            'upvotes',
            'author',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'creation_date': {'read_only': True},
            'upvotes': {'read_only': True},
        }


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'author',
            'content',
            'creation_date',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'creation_date': {'read_only': True},
        }
