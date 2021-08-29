from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer
from .models import Post
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import (
    authentication_classes,
    permission_classes,
    api_view
)
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'


# Create your views here.


@api_view(['GET', ])
def api_get_posts_view(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        print(post)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        print(serializer.data)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)


@api_view(['POST', ])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def api_create_posts_view(request):
    if request.method == 'POST':

        data = request.data
        data['author'] = request.user.pk
        print(data)
        serializer = PostCreateSerializer(data=data)

        data = {}
        if serializer.is_valid():
            blog_post = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['title'] = blog_post.title
            data['content'] = blog_post.content
            data['slug'] = blog_post.slug
            data['username'] = blog_post.author.username
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Url: https://<your-domain>/api/blog/<slug>/update
# Headers: Authorization: Token <token>
@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def api_update_blog_view(request, slug):
    try:
        blog_post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response': "You don't have permission to edit that."})
    print(user)
    if request.method == 'PUT':
        serializer = PostUpdateSerializer(blog_post, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = UPDATE_SUCCESS
            data['title'] = blog_post.title
            data['content'] = blog_post.content
            data['slug'] = blog_post.slug
            data['date_updated'] = blog_post.date_updated
            data['username'] = blog_post.author.username
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiBlogListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'content', 'author__username')
