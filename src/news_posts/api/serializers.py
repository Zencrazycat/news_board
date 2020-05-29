from rest_framework import serializers

from news_posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    pass


class CommentSerializer(serializers.ModelSerializer):
    pass
