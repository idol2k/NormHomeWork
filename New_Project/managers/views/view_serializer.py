from ..models import Posts
from ..serializer.detail_serializer import PostsUserSerializer
from rest_framework import mixins
from rest_framework import generics


class PostsUserView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
