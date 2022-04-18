import json

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework import mixins

from session.api.serializers import SessionDataSerializer
from session.models import SessionData


class LiveScoreConsumer(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericAsyncAPIConsumer):
    queryset = SessionData.objects.all()
    serializer_class = SessionDataSerializer
