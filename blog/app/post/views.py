from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer
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
# Create your views here.


@api_view(['POST', ])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def api_post_view(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        print(post)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        print("here 3")
        serializer = PostSerializer(post)
        print(serializer.data)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)
