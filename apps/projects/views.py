from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from projects.models import Projects
from projects.serializers import ProjectsCreateSerializer, ProjectsUpdateSerializer, ProjectsRetrieveSerializer, ProjectsSerializer, ProjectsListSerializer


class ProjectsViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, ModulePermission)
    queryset = Projects.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectsListSerializer
        elif self.action == 'create':
            return ProjectsCreateSerializer
        elif self.action in ('update', 'partial_update'):
            return ProjectsUpdateSerializer
        elif self.action == 'retrieve':
            return ProjectsRetrieveSerializer
        else:
            return ProjectsSerializer

    @action(detail=False)
    def get_project(self, request):
        """
        通过专利id获取项目
        """
        empty_order = Projects.objects.filter(projects_patents=request.query_params.get('patents'))
        serializer = self.get_serializer(empty_order, many=True)
        return Response(serializer.data)