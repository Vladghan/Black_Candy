from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from session.api.serializers import SessionListSerializer
from session.models import UserSession


class SessionView(generics.ListAPIView):
    serializer_class = SessionListSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'

    def get_queryset(self):
        sessions = UserSession.objects.filter(user=self.request.user.pk)
        return sessions
