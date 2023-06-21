from rest_framework import viewsets
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
