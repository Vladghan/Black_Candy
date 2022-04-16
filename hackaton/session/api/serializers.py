from rest_framework import serializers

from session.models import Session, SessionData, UserSession


class SessionDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionData
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    sessions_data = SessionDataListSerializer(many=True)

    class Meta:
        model = Session
        fields = '__all__'


class SessionUserListSerializer(serializers.ModelSerializer):
    session = SessionSerializer()

    class Meta:
        model = UserSession
        fields = '__all__'
