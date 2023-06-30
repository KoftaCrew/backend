from rest_framework import viewsets, permissions, response, mixins

from question.filters import IsExamFilterBackendForGetMethod
from student_answer.models import StudentAnswer, Answer
from student_answer.serializers import StudentAnswerSerializer, AnswerSerializer
from student_answer.filters import IsExamFilterBackendForGetMethodL1, IsExamFilterBackendForDeleteMethod


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


class AnswerViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Answer.objects.all().order_by('-id')
    serializer_class = AnswerSerializer
    lookup_field = 'id'
    filter_backends = [IsExamFilterBackendForGetMethodL1]
