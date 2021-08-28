from django.urls import path
from .views import api_post_view

app_name = 'post'

urlpatterns = [
    path('<slug>/', api_post_view, name='detail')
]