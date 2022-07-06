from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from messagesText.api.serializers import MessagesTextCreateSerializer


class MessagesTextViewSet(ViewSet):
    def create(self, request):
        username = MessagesTextCreateSerializer(data=request.POST)
        username.is_valid(raise_exception=True)
        username.save()
        return Response(status=status.HTTP_200_OK, data=username.data)