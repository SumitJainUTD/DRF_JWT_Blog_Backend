from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post
from django.http import JsonResponse
# Create your views here.


@api_view(['GET', ])
def api_post_view(request, slug):
    print("here test")
    try:
        post = Post.objects.get(slug=slug)
        print(post)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    print("here 2")
    if request.method == 'GET':
        print("here 3")
        serializer = PostSerializer(post)
        print(serializer.data)
        return JsonResponse(serializer.data)
        # return Response(serializer.data)
