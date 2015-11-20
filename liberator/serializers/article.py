from rest_framework import serializers

from liberator import models

from .issue import * 
from .section import * 
from .user import * 
from .comment import * 
#from .content import * 

class ArticleSerializer(serializers.ModelSerializer):
    
    authors = serializers.StringRelatedField(many=True)
    section = serializers.StringRelatedField()
    issues = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    contents = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='content-detail'
    )
    comments = CommentSerializer(many=True)

    class Meta:
        model = models.Article
        fields = (
            "id",
            "authors", 
            "section",
            "issues",
            "comments",
            "contents",
        )
