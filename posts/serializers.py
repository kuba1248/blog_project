from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_["author"] = instance.author.username
        dict_["likes"] = instance.likes.all().count()
        dict_["comments"] = CommentSerializer(instance.comments.all(), many=True).data
        return dict_


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['post']

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_["author"] = instance.author.username
        return dict_


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer): # new

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)