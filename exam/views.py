from rest_framework import viewsets, permissions, mixins
from exam.serializers import ExamSerializer, StudentExamDTOSerializer, ExamCardSerializer
from exam.models import Exam


# Create your views here.

class ExamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows edits on exams
    """
    queryset = Exam.objects.all().order_by('-created_at')
    serializer_class = ExamSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.id)

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

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class StudentExamViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin
):
    queryset = Exam.objects.all().order_by('-created_at')
    serializer_class = StudentExamDTOSerializer
    lookup_field = 'id'


class ExamCardViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin
):
    queryset = Exam.objects.all().order_by('-created_at')
    serializer_class = ExamCardSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.action == 'list' or self.action == 'update' or self.action == 'partial_update':
            return [permissions.IsAuthenticated(), ]
        return super().get_permissions()

    def get_queryset(self):
        if self.action == 'list' or self.action == 'update' or self.action == 'partial_update':
            return self.queryset.filter(user_id=self.request.user.id)
        return self.queryset


