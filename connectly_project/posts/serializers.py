from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import User, Post, Comment, Like

# Serializers with Validation
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}  # Hide password in response

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='like_count', read_only=True)
    comment_count = serializers.IntegerField(source='comment_count', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'created_at', 'like_count', 'comment_count']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'post', 'created_at']