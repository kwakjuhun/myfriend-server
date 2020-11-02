from rest_framework import serializers
from .models import Talk

class talkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ('talk',)