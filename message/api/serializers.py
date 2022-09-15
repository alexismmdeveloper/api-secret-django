from rest_framework.serializers import ModelSerializer
from message.models import Messages

class MessageSerializers(ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
