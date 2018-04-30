from rest_framework import serializers

class ReqSerializer(serializers.Serializer):
  tag = serializers.CharField()