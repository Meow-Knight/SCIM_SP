from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ScimViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        return Response({'message': ''})
