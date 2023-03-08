from rest_framework import serializers
from post import models


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'
