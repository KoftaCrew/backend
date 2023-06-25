from rest_framework import viewsets
from model_answer.serializers import ModelAnswerSerializer, KeyPhraseSerializer
from model_answer.models import ModelAnswer, KeyPhrase


# Create your views here.


class ModelAnswerViewSet(viewsets.ModelViewSet):
    queryset = ModelAnswer.objects.all().order_by('-created_at')
    serializer_class = ModelAnswerSerializer
    lookup_field = 'id'


class KeyPhraseViewSet(viewsets.ModelViewSet):
    queryset = KeyPhrase.objects.all().order_by('-created_at')
    serializer_class = KeyPhraseSerializer
    lookup_field = 'id'
