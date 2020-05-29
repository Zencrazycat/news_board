from django.urls import path

from news_posts.api import views

app_name = 'api-posts'

urlpatterns = [
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
    path('post/<int:pk>/comments/', views.CommentsView.as_view(), name='comments'),
    path('post/<int:pk1>/comment/<int:pk2>/', views.CommentView.as_view(), name='comment'),
]
