from rest_framework import viewsets
from rest_framework import permissions

from question.filters import IsExamFilterBackend
from question.models import Question
from question.serializers import QuestionSerializer


# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows edits on exams.
    """
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    lookup_field = 'id'
    filter_backends = [IsExamFilterBackend]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        self.queryset = self.queryset.exclude(exam__mode=2)
        ret = super().update(request, *args, **kwargs)
        self.queryset = Question.objects.all().order_by('-created_at')
        return ret

    def partial_update(self, request, *args, **kwargs):
        self.queryset = self.queryset.exclude(exam__mode=2)
        ret = super().partial_update(request, *args, **kwargs)
        self.queryset = Question.objects.all().order_by('-created_at')
        return ret

    def destroy(self, request, *args, **kwargs):
        self.queryset = self.queryset.exclude(exam__mode=2)
        ret = super().destroy(request, *args, **kwargs)
        self.queryset = Question.objects.all().order_by('-created_at')
        return ret
