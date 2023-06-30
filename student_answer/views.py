from rest_framework import viewsets, permissions, mixins

from question.filters import IsExamFilterBackendForGetMethod
from student_answer.models import StudentAnswer
from student_answer.serializers import StudentAnswerSerializer, UpdateStudentAnswerSerializer
from student_answer.filters import IsExamFilterBackendForDeleteMethod


class StudentAnswerViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = StudentAnswer.objects.all().order_by('-id')
    serializer_class = StudentAnswerSerializer
    lookup_field = 'student_id'
    filter_backends = [IsExamFilterBackendForGetMethod, IsExamFilterBackendForDeleteMethod]

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return permissions.AllowAny(),
        if self.action != 'create':
            return [permissions.IsAuthenticated(), ]
        return super().get_permissions()


class UpdateStudentAnswerViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    queryset = StudentAnswer.objects.all().order_by('-id')
    serializer_class = UpdateStudentAnswerSerializer
    lookup_field = 'id'
