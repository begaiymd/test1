from itertools import count
from rest_framework import serializers

from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_['user'] = instance.user.username
        
        dict_['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        dict_['comments1'] = CommentSerializer(instance.comments.all(), many=True).data

        return dict_

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['post']
        exclude = ['post1']


    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_['user'] = instance.user.username
        return dict_



