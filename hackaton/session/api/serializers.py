from rest_framework import serializers

from session.models import Session, SessionData, UserSession


class SessionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionData
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    sessions_data = SessionDataSerializer(many=True)

    class Meta:
        model = Session
        fields = '__all__'


class SessionUserListSerializer(serializers.ModelSerializer):
    session = SessionSerializer()

    class Meta:
        model = UserSession
        fields = '__all__'
