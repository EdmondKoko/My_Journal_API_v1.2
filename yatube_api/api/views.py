from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets, exceptions

from api.permissions import AuthorOrReadOnly
from api.serializers import FollowSerializer, GroupSerializer
from api.serializers import PostSerializer, CommentSerializer
from posts.models import Post, Follow, Group

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AuthorOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post_id = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        new_queryset = post_id.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        serializer.save(
            author=self.request.user,
            post=post
        )

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied('Изменение чужого контента '
                                              'запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(CommentViewSet, self).perform_destroy(instance)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        new_queryset = user.follower.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        super(FollowViewSet, self).perform_create(serializer)
