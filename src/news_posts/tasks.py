from celery import shared_task

from news_posts.models import Post


@shared_task(bind=True)
def reset_upvotes():
    posts = Post.objects.filter(upvotes__gt=0)
    for post in posts:
        post.upvotes = 0
        post.save()
