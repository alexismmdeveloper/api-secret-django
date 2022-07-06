from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from username.models import Username
from messagesText.api.serializers import MessagesTextSerializer

class UsernameSerializer(ModelSerializer):
    messages = MessagesTextSerializer(many=True, read_only=True)
    class Meta:
        model = Username
        fields = ['id', 'username', 'messages']

