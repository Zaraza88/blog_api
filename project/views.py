from django.forms import ValidationError
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response

from .serializers import (
    CommentCreateSerializars,
    CommentDetailSerealizers,
    LikesSerializers,
    PostSerializaers, 
    CommentViewSerealizers,
    PostCreateSerializers,
    PostDetaiSerializaers)
from .models import Comment, Like, Post


class PostView(generics.ListAPIView):
    """Вывод постов"""
    serializer_class = PostSerializaers
    queryset = Post.objects.all().only('id', 'title', 'author')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostCreateView(generics.CreateAPIView):
    """Добавления постов"""
    serializer_class = PostCreateSerializers
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDeteilView(generics.RetrieveUpdateAPIView):
    """Вывод детальной информации о посте"""
    serializer_class = PostDetaiSerializaers
    queryset = Post.objects.all().prefetch_related('post_comment')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CreateComment(generics.ListCreateAPIView):
    """Добавление комментарий к посту или к комментариям"""
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializars
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(name=self.request.user)


class CommentsOnASpecificPostView(generics.RetrieveAPIView):
    """Вывод всех комментариев конкретного поста"""
    serializer_class = CommentDetailSerealizers

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs.get('pk'))


class GetNestedComment(generics.RetrieveAPIView):
    """Вывод вложенных комментариев до 3 уровня """ 
    serializer_class = CommentViewSerealizers
  
    def get_queryset(self):
        return Comment.objects.filter(id=self.kwargs.get('pk'))


class CreateLikeDislike(generics.CreateAPIView):
    """Поставить лайк/дизлайк"""
    queryset = Like.objects.all()
    serializer_class = LikesSerializers
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            self.perform_create(serializers)
            return Response(status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)