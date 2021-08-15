from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from search import models, serializers


class StudiosViewSet(ModelViewSet):
    queryset = models.Studio.objects.all()
    serializer_class = serializers.StudioSerializer
