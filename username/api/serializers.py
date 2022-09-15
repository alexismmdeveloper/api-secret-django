from rest_framework.serializers import ModelSerializer
from username.models import Username

class UsernameSerializers(ModelSerializer):
    class Meta:
        model = Username
        fields = '__all__'