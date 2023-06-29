from rest_framework import serializers
from question.models import Question
from model_answer.serializers import ModelAnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    question_model_answer = ModelAnswerSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = Question
        optional_fields = ['exam', ]
        fields = ['id', 'question', 'question_model_answer', 'created_at', 'updated_at']
