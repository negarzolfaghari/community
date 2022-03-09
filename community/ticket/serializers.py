from rest_framework import serializers
from ticket.models import Message
from ticket.models import Thread

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Thread
        fields=['pk','created', 'category', 'ticket_id','user1','user2' ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=['pk','created', 'last_updated', 'message', 'file', 'status', 'direction', 'thread']