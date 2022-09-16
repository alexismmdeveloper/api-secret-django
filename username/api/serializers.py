from rest_framework.serializers import ModelSerializer
from username.models import Username
from message.api.serializers import MessageSerializers

class UsernameSerializer(ModelSerializer):
    messages = MessageSerializers(many=True, read_only=True)
    class Meta:
        model = Username
        fields = ['id', 'username', 'messages']
