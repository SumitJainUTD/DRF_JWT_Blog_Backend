import uuid

from rest_framework import serializers
from .models import Post

MIN_TITLE_LENGTH = 5
MIN_BODY_LENGTH = 5


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'slug']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'slug']

    def save(self):

        try:
            print(self.validated_data)
            title = self.validated_data['title']
            if len(title) < MIN_TITLE_LENGTH:
                raise serializers.ValidationError(
                    {"response": "Enter a title longer than " + str(MIN_TITLE_LENGTH) + " characters."})
            print(title)
            body = self.validated_data['content']
            if len(body) < MIN_BODY_LENGTH:
                raise serializers.ValidationError(
                    {"response": "Enter a body longer than " + str(MIN_BODY_LENGTH) + " characters."})
            print(body)
            slug = self.validated_data['slug']
            print(slug)
            blog_post = Post(
                id=uuid.uuid4(),
                author=self.validated_data['author'],
                title=title,
                content=body,
                slug = slug
            )

            blog_post.save()
            return blog_post
        except KeyError:
            raise serializers.ValidationError({"response": "You must have a title, some content, and an image."})
