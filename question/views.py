import django_filters.rest_framework
from rest_framework import viewsets
from question.serializers import QuestionSerializer
from question.models import Question
from question.filters import IsExamFilterBackend

# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows edits on exams.
    """
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    lookup_field = 'id'
    filter_backends = [IsExamFilterBackend]
