from django.urls import path
from .views import (
    api_get_posts_view,
    api_create_posts_view,
    ApiBlogListView,
    api_update_blog_view
)

app_name = 'post'

urlpatterns = [
    path('<slug>/', api_get_posts_view, name='detail'),
    path('<slug>/update', api_update_blog_view, name="update"),
    path('create', api_create_posts_view, name='create_post'),
    path('list', ApiBlogListView.as_view(), name="list"),
]
