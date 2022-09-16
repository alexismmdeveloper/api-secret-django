from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from username.models import Username
from username.api.serializers import UsernameSerializer

class UserNameViewSet(ViewSet):
    def retrieve(self, request , pk):
        user = UsernameSerializer(Username.objects.get(username=pk))
        return Response(status=status.HTTP_200_OK, data=user.data)

    def create(self, request):
        username = UsernameSerializer(data=request.data)
        username.is_valid(raise_exception=True)
        username.save()
        return Response(status=status.HTTP_200_OK, data=username.data)