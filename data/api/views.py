from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from data.api.serializers import DataSerializers

class DataViewSet(ViewSet):
    def create(self, request):
        data_response = DataSerializers(data=request.data)
        data_response.is_valid(raise_exception=True)
        data_response.save()
        return Response(status=status.HTTP_200_OK, data=data_response.data)