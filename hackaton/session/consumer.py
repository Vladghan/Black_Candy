import json

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework import mixins

from .models import Session
from .api.serializers import SessionSerializer


class LiveScoreConsumer(mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.PatchModelMixin,
        mixins.UpdateModelMixin,
        mixins.CreateModelMixin,
        mixins.DeleteModelMixin,
        GenericAsyncAPIConsumer):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

