from rest_framework import serializers
from bb_post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'subject', 'content')
