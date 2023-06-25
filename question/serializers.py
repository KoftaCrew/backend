from rest_framework import serializers
from question.models import Question
from model_answer.serializers import ModelAnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    question_model_answer = ModelAnswerSerializer(many=False)

    class Meta:
        model = Question
        fields = '__all__'
