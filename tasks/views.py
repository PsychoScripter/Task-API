from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from tasks.models import Task
from tasks.serializers import TasksSerializer
# Create your views here.

class TaskListAPIView(ListCreateAPIView):
    def get_queryset(self):
        is_done = self.request.query_params.get('is_done', None)
        if is_done is not None:
            return Task.objects.filter(is_done=is_done)
        return Task.objects.all()

    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TasksSerializer

class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer


