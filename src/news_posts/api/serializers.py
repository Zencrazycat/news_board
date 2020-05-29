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
