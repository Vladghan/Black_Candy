from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from session.api.serializers import SessionUserListSerializer, SessionSerializer
from session.models import UserSession, Session


class SessionView(generics.ListAPIView):
    serializer_class = SessionUserListSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        sessions = UserSession.objects.filter(user=self.request.user.pk)
        return sessions


class SessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SessionSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Session.objects.all()

