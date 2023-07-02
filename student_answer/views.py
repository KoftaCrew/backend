from rest_framework import viewsets, permissions, mixins, response, status
from django.core.exceptions import ValidationError

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
    queryset = StudentAnswer.objects.all().filter(exam__mode=3).order_by('-id')
    serializer_class = StudentAnswerSerializer
    lookup_field = 'student_id'
    filter_backends = [IsExamFilterBackendForGetMethod, IsExamFilterBackendForDeleteMethod]

    def get_permissions(self):
        if self.action != 'create':
            return [permissions.IsAuthenticated(), ]
        return super().get_permissions()

    def get_queryset(self):
        if self.action != 'create':
            return self.queryset.filter(exam__user_id=self.request.user.id)
        return self.queryset

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as err:
            return response.Response(
                {
                    'detail': err.message
                },
                status=status.HTTP_403_FORBIDDEN
            )


class UpdateStudentAnswerViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    queryset = StudentAnswer.objects.all().filter(
        is_submitted=False,
        exam__mode=3
    ).order_by('-id')
    serializer_class = UpdateStudentAnswerSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as err:
            return response.Response(
                {
                    'detail': err.message
                },
                status=status.HTTP_403_FORBIDDEN
            )
