from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import CianCoders

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = CianCoders.objects.all()