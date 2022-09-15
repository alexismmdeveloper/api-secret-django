from username.models import Username
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from username.api.serializers import UsernameSerializers

class UsernameView(APIView):
    def post(self, request):
        serializer = UsernameSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)