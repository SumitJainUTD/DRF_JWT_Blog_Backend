from django.urls import path
from .views import (
    api_get_posts_view,
    api_create_posts_view,
    ApiBlogListView,
    api_update_blog_view,
    api_get_health

)

app_name = 'post'

urlpatterns = [
    path('health/', api_get_health, name='health'),
    path('<slug>/', api_get_posts_view, name='detail'),
    path('<slug>/update', api_update_blog_view, name="update"),
    path('create', api_create_posts_view, name='create'),
    path('list', ApiBlogListView.as_view(), name="list"),
]
