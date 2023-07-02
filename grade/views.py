from rest_framework import viewsets, mixins, permissions
from exam.models import Exam
from grade.serializers import StartGradingTriggerSerializer


class StartGradingTriggerViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    queryset = Exam.objects.all().filter(mode=3)
    serializer_class = StartGradingTriggerSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

