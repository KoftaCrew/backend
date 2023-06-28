from rest_framework import viewsets, permissions
from model_answer.serializers import ModelAnswerSerializer, KeyPhraseSerializer
from model_answer.models import ModelAnswer, KeyPhrase
from question.models import Question
from rest_framework import response


# Create your views here.


class ModelAnswerViewSet(viewsets.ModelViewSet):
    queryset = ModelAnswer.objects.all().order_by('-created_at')
    serializer_class = ModelAnswerSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(question__exam__user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        if  Question.objects.get(id=request.data.get('question', -1)).exam.user_id == request.user.id:
            return super().create(request, *args, **kwargs)
        return response.Response({
            'details': "You aren't able to edit this exam"
        })


class KeyPhraseViewSet(viewsets.ModelViewSet):
    queryset = KeyPhrase.objects.all().order_by('-created_at')
    serializer_class = KeyPhraseSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(model_answer__question__exam__user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        if ModelAnswer.objects.get(id=request.data.get('question', -1)).question.exam.user_id == request.user.id:
            return super().create(request, *args, **kwargs)
        return response.Response({
            'details': "You aren't able to edit this exam"
        })
