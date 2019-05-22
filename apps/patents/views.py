from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from patents.models import Patents

from patents.serializers import PatentsCreateSerializer, PatentsUpdateSerializer, PatentsRetrieveSerializer, PatentsSerializer, PatentsListSerializer


class PatentsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, ModulePermission)
    queryset = Patents.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PatentsListSerializer
        elif self.action == 'create':
            return PatentsCreateSerializer
        elif self.action in ('update', 'partial_update'):
            return PatentsUpdateSerializer
        elif self.action == 'retrieve':
            return PatentsRetrieveSerializer
        else:
            return PatentsSerializer
