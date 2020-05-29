from django.urls import path

from news_posts.api import views

app_name = 'api-posts'

urlpatterns = [
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),

    path('post/<int:pk>/comments/', views.PostCommentsView.as_view(), name='post-comments'),

    path('comments/', views.CommentsView.as_view(), name='comments'),
    path('comment/<int:pk>/', views.CommentView.as_view(), name='comment'),
]
