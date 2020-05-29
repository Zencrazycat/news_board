from django.contrib import admin
from django.urls import path, include


API_PREFIX = 'api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path(f'{API_PREFIX}/news_posts/', include('news_posts.api.urls')),
]
