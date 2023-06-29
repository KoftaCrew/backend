from rest_framework import serializers
from django.db import transaction

from question.models import Question
from model_answer.serializers import ModelAnswerSerializer
from model_answer.models import ModelAnswer


class QuestionSerializer(serializers.ModelSerializer):
    model_answer = ModelAnswerSerializer(
        many=False
    )

    class Meta:
        model = Question
        depth = 3
        optional_fields = ['exam', ]
        fields = ['id', 'question', 'model_answer', 'created_at', 'updated_at']

    @transaction.atomic
    def update(self, instance: Question, validated_data: dict) -> Question:
        for attr, value in validated_data.items():
            if attr != 'model_answer':
                setattr(instance, attr, value)
        model_answer_serializer = ModelAnswerSerializer()
        new_model_answer: ModelAnswer = ModelAnswerSerializer.create(
            model_answer_serializer,
            validated_data.get('model_answer', {})
        )
        instance.model_answer = new_model_answer
        instance.save()

        return instance

    @transaction.atomic
    def create(self, validated_data: dict) -> Question:
        instance: Question = Question.objects.create(
            question=validated_data.get('question', None),
            exam=validated_data.get('exam', -1)
        )
        model_answer_serializer = ModelAnswerSerializer()
        new_model_answer: ModelAnswer = ModelAnswerSerializer.create(
            model_answer_serializer,
            validated_data.get('model_answer', {})
        )
        instance.save()
        instance.model_answer = new_model_answer
        instance.save()
        return instance
