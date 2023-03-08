from rest_framework import viewsets
from post import models, serializers


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
