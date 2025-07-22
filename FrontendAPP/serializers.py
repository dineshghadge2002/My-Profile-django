from rest_framework import serializers

class AddSerializer(serializers.Serializer):
    num1 = serializers.FloatField()
    num2 = serializers.FloatField()

class ChatSerializer(serializers.Serializer):
    user_input = serializers.CharField()