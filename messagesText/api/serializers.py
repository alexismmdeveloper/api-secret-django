from rest_framework.serializers import ModelSerializer
from messagesText.models import Messages

class MessagesTextSerializer(ModelSerializer):
    class Meta:
        model = Messages
        fields = ['messageText']

class MessagesTextCreateSerializer(ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'