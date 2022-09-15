from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from message.api.serializers import MessageSerializers

class MessagesViewSet(ViewSet):
    def create(self, request):
        username = MessageSerializers(data=request.data)
        username.is_valid(raise_exception=True)
        username.save()
        return Response(status=status.HTTP_200_OK, data=username.data)