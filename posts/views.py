from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .models import Post, Comment, Like
from .permissions import IsAuthorOrReadOnly  # new
from .serializers import PostSerializer, UserSerializer, CommentSerializer, LikeSerializer
from rest_framework import viewsets


# class PostList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    # new
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    # new
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class UserViewSet(viewsets.ModelViewSet):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
