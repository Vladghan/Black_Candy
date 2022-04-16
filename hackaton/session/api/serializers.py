from rest_framework import serializers

from session.models import Session, SessionData


class SessionDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionData
        fields = '__all__'


class SessionListSerializer(serializers.ModelSerializer):
    sessions_data = SessionDataListSerializer(many=True)

    class Meta:
        model = Session
        fields = '__all__'

