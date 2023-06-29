from rest_framework import serializers
from model_answer.models import ModelAnswer, KeyPhrase
from django.db import transaction


class KeyPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyPhrase
        depth = 1
        fields = '__all__'


class ModelAnswerSerializer(serializers.ModelSerializer):
    model_answer_key_phrases = KeyPhraseSerializer(
        many=True,
        required=False
    )

    class Meta:
        model = ModelAnswer
        depth = 2
        optional_field = ['model_answer_key_phrases',]
        fields = ['id', 'text', 'created_at', 'updated_at', 'model_answer_key_phrases']

    @transaction.atomic
    def create(self, validated_data: dict) -> ModelAnswer:
        instance: ModelAnswer = ModelAnswer.objects.create(
            text=validated_data.get('text', None),
        )
        key_phrase_serializer = KeyPhraseSerializer()
        for value in validated_data.get('model_answer_key_phrases', []):
            value['model_answer'] = instance
            KeyPhraseSerializer.create(key_phrase_serializer, value)
        instance.save()
        return instance
