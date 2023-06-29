from rest_framework import serializers
from model_answer.models import ModelAnswer, KeyPhrase


class KeyPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyPhrase
        fields = '__all__'


class ModelAnswerSerializer(serializers.ModelSerializer):
    model_answer_key_phrases = KeyPhraseSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = ModelAnswer
        fields = ['id', 'text', 'created_at', 'updated_at', 'model_answer_key_phrases']

