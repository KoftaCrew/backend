from rest_framework import viewsets, permissions
from exam.serializers import ExamSerializer
from exam.models import Exam


# Create your views here.

class ExamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows edits on exams
    """
    queryset = Exam.objects.all().order_by('-created_at')
    serializer_class = ExamSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        self.queryset = self.queryset.exclude(mode=2)
        ret = super().update(request, *args, **kwargs)
        self.queryset = Exam.objects.all().order_by('-created_at')
        return ret

    def partial_update(self, request, *args, **kwargs):
        self.queryset = self.queryset.exclude(mode=2)
        ret = super().partial_update(request, *args, **kwargs)
        self.queryset = Exam.objects.all().order_by('-created_at')
        return ret

    def destroy(self, request, *args, **kwargs):
        self.queryset = self.queryset.exclude(mode=2)
        ret = super().destroy(request, *args, **kwargs)
        self.queryset = Exam.objects.all().order_by('-created_at')
        return ret

