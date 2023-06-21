from rest_framework import serializers
from model_answer.models import ModelAnswer, KeyPhrase


class ModelAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelAnswer
        fields = [
            'question',
            'text',
            'created_at',
            'updated_at',
        ]


class KeyPhraseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KeyPhrase
        fields = [
            'model_answer',
            'text',
            'created_at',
            'updated_at',
        ]
