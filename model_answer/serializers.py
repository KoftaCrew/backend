from rest_framework import serializers
from model_answer.models import ModelAnswer, KeyPhrase


class ModelAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelAnswer
        fields = '__all__'


class KeyPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyPhrase
        fields = '__all__'
