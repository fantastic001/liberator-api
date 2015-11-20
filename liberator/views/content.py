
from rest_framework import viewsets
from liberator import serializers


class ContentViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CommentSerializer

    queryset = serializer_class.Meta.model.objects.all()
