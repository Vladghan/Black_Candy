from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from session.api.serializers import SessionUserListSerializer, SessionSerializer, SessionDataSerializer, \
    SessionUserDetailSerializer
from session.models import UserSession, Session, SessionData


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


class SessionDataView(generics.ListCreateAPIView):
    serializer_class = SessionDataSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SessionData.objects.all()


class SessionDataDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = SessionUserDetailSerializer
    # authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    # queryset = SessionData.objects.all()

    def get_queryset(self):
        queryset = SessionData.objects.filter(pk=self.kwargs.get('pk'))
        return queryset
